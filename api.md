# Courts

Types:

```python
from court_listener_sdk.types import Court
```

Methods:

- <code title="get /courts/{id}/">client.courts.<a href="./src/court_listener_sdk/resources/courts.py">retrieve</a>(id, \*\*<a href="src/court_listener_sdk/types/court_retrieve_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/court.py">Court</a></code>
- <code title="get /courts/">client.courts.<a href="./src/court_listener_sdk/resources/courts.py">list</a>(\*\*<a href="src/court_listener_sdk/types/court_list_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/court.py">SyncCursorURLPage[Court]</a></code>

# Dockets

Types:

```python
from court_listener_sdk.types import Docket
```

Methods:

- <code title="get /dockets/{id}/">client.dockets.<a href="./src/court_listener_sdk/resources/dockets.py">retrieve</a>(id, \*\*<a href="src/court_listener_sdk/types/docket_retrieve_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/docket.py">Docket</a></code>
- <code title="get /dockets/">client.dockets.<a href="./src/court_listener_sdk/resources/dockets.py">list</a>(\*\*<a href="src/court_listener_sdk/types/docket_list_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/docket.py">SyncCursorURLPage[Docket]</a></code>

# Clusters

Types:

```python
from court_listener_sdk.types import Cluster
```

Methods:

- <code title="get /clusters/{id}/">client.clusters.<a href="./src/court_listener_sdk/resources/clusters.py">retrieve</a>(id, \*\*<a href="src/court_listener_sdk/types/cluster_retrieve_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/cluster.py">Cluster</a></code>
- <code title="get /clusters/">client.clusters.<a href="./src/court_listener_sdk/resources/clusters.py">list</a>(\*\*<a href="src/court_listener_sdk/types/cluster_list_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/cluster.py">SyncCursorURLPage[Cluster]</a></code>

# Opinions

Types:

```python
from court_listener_sdk.types import Opinion
```

Methods:

- <code title="get /opinions/{id}/">client.opinions.<a href="./src/court_listener_sdk/resources/opinions.py">retrieve</a>(id, \*\*<a href="src/court_listener_sdk/types/opinion_retrieve_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/opinion.py">Opinion</a></code>
- <code title="get /opinions/">client.opinions.<a href="./src/court_listener_sdk/resources/opinions.py">list</a>(\*\*<a href="src/court_listener_sdk/types/opinion_list_params.py">params</a>) -> <a href="./src/court_listener_sdk/types/opinion.py">SyncCursorURLPage[Opinion]</a></code>
