**Summary**: python_project_template is a pure-Python analytcs server built to track Python usage patterns, as well as demonstrate key Python best practices.

.. contents::
   :depth: 2
   :backlinks: top
   :local:

Quick Start
-----------

**Note: Aspire to make your project easy to run, but if it's not, describe the development and environment setup process in a separate document.**

* Clone the project (or download a zip archive)
```bash
git clone git@github.com:erfankashani/python_project_template.git
```

* Install Dependencies
```bash
pip install -r requirements
```

* Optional: Install the package for dev mode
```bash
pip install -e .
```

Contacts
--------

**Note: Include stakeholders by individual name (and email), as well as group (and mailing list) whenever possible. People go on vacation.**

* Lead developer: Erfan K (https://github.com/erfankashani/python_project_template)
* Development manager: 
* QA: 
* Operations contact: 
* Architect: 

**Note: If a group touches this project, at least one name should go on here. System administration, network operations, information security, UX/design, etc.**

Timelines
---------

**Note: Depending on the state of the project you can move this section up or down, but best not to remove it. A history/timeline helps orient readers.**

Example:
* August 17, 2015: Document created
* September 23, 2015: Project proposal presented (link)
* October 1, 2015: Implementation and design phase start
* November 17, 2015: Code complete
* November 24, 2015: Testing complete
* December 2, 2015: Production throttle

Monitoring
----------

* Production monitoring link
* Production log reports link

* Development reports link

Production load balancer is at espyserv.prod.example.com. Logs can
also be found on the local filesystem at ``/var/logs/python_project_template``.

Code repo link

Specifications
--------------

Called by the storefront service. Primarily read-only. Write frequency
is <1000 per day by batch.

* *Traffic*: (Nov 2015) 100,000 queries per day on average. Traffic peaks at
  12:00 PST around 500 requests per minute.
* *Latency*: (Nov 2015) Varies based on query and endpoint. Median is 30ms and
  95th percentile is 500ms.

Environment
-----------

python_project_template is developed locally, but runs in production. In
production we have one pool: espyserv. This pool comprises 200
machines spread across 3 datacenters.

Dependencies
------------

python_project_template is a backend service and has relatively few dependencies, both
in terms of upstream services and code.

Services
~~~~~~~~

**Storage**: python_project_template depends on production storage servers and
will experience a total outage in the event of storage
failure. Restoration of services will require a restart of the python_project_template
service.

**Logging**: Achieved through ERLS (Example Remote Logging
Service). Restoration of python_project_template logging is internal and automatic,
requiring no operations action.

Libraries
~~~~~~~~~

In production, python_project_template packages all of its libraries. For
development, see requirements.txt. python_project_template is tested on Python 3.8.

Architecture
------------

(Example)
Python WSGI application to service HTTP requests. Data is stored
in-memory in a SQLite database.

Given that data is not sensitive and all clients are internal,
security is by firewall only.

Testing strategy
----------------

(Example)
* Unit tests are in the /tests/ directory, run with py.test
* Manual acceptance test achieve via browser in staging environment
* Production traffic testing (for throttle): trigger with the Example flow

Tickets
-------

Important tickets of record.

(Example)
* Provision the pool
* Schema review
* Security architecture review
* Network topology setup
* Firewall exceptions
* Firewall exceptions #2 for real this time


Please note: this template was taken from EspyMetrics project. please checkout the author's work [here](https://github.com/mahmoud/espymetrics/blob/master/DESIGN.rst).