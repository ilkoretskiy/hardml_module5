import redis
from retry import retry

class ServiceDiscovery:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self._client = redis.Redis(
            host=host,
            port=port,
            db=0,
            password=password
        )

    def register(self, replica_name, service_host, service_port):
        self._client.lpush("web_app", replica_name)
        self._client.hset(name = replica_name, key="host", value=service_host)
        self._client.hset(name = replica_name, key="port", value=service_port)

    @retry(redis.exceptions.ConnectionError, tries=3, delay=2) 
    def unregister(self, replica_name):        
        self._client.lrem(name="web_app", count=1, value=replica_name)
        self._client.hdel(replica_name, "host", "port")


_service_discovery = None

def init_and_get_service_discovery(host, port, password) -> ServiceDiscovery:
    global _service_discovery
    _service_discovery = ServiceDiscovery(host, port, password)
    return  _service_discovery

def get_service_discovery() -> ServiceDiscovery:
    return _service_discovery

