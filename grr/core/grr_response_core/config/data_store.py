#!/usr/bin/env python
"""Configuration parameters for the data stores."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from grr_response_core.lib import config_lib

config_lib.DEFINE_integer("Datastore.maximum_blob_size", 512 * 1024,
                          "Maximum blob size we may store in the datastore.")

config_lib.DEFINE_string("Datastore.implementation", "FakeDataStore",
                         "Storage subsystem to use.")

config_lib.DEFINE_string("Blobstore.implementation", "MemoryStreamBlobStore",
                         "Blob storage subsystem to use.")

config_lib.DEFINE_string("Database.implementation", "",
                         "Relational database system to use.")

config_lib.DEFINE_bool(
    "Database.enabled", False,
    "Use relational database for reading as well as for writing.")

config_lib.DEFINE_bool("Database.aff4_enabled", True,
                       "Enables reading/writing to the legacy data store.")

config_lib.DEFINE_string(
    "Datastore.location",
    default="%(Config.prefix)/var/grr-datastore",
    help=("Location of the data store (usually a "
          "filesystem directory)"))

# SQLite data store.
# NOTE: The SQLite datastore was obsoleted, so these options do not get
# used. We can remove them once users have migrated to MySQL.
config_lib.DEFINE_integer(
    "SqliteDatastore.vacuum_check",
    default=10,
    help=("Number of rows that need to be deleted before "
          "checking if the sqlite file may need to be "
          "vacuumed."))

config_lib.DEFINE_integer(
    "SqliteDatastore.vacuum_frequency",
    default=60,
    help=("Minimum interval (in seconds) between vacuum"
          "operations on the same sqlite file."))

config_lib.DEFINE_integer(
    "SqliteDatastore.vacuum_minsize",
    default=10 * 1024,
    help=("Minimum size of sqlite file in bytes required"
          " for vacuuming"))

config_lib.DEFINE_integer(
    "SqliteDatastore.vacuum_ratio",
    default=50,
    help=("Percentage of pages that are free before "
          "vacuuming a sqlite file."))

config_lib.DEFINE_integer(
    "SqliteDatastore.connection_cache_size",
    default=1000,
    help=("Number of file handles kept in the SQLite "
          "data_store cache."))

# MySQL configuration (relational database and legacy MySQLAdvancedDataStore).
config_lib.DEFINE_string("Mysql.host", "localhost",
                         "The MySQL server hostname.")

config_lib.DEFINE_integer("Mysql.port", 0, "The MySQL server port.")

config_lib.DEFINE_string(
    "Mysql.username",
    default="root",
    help="The user to connect to the database.")

config_lib.DEFINE_string(
    "Mysql.password",
    default="",
    help="The password to connect to the database.")

config_lib.DEFINE_string(
    "Mysql.database", default="grr_db", help="Name of the database to use.")

config_lib.DEFINE_integer(
    "Mysql.conn_pool_max",
    default=10,
    help="The maximum number of open connections to keep available in the pool."
)

config_lib.DEFINE_string(
    "Mysql.migrations_dir", "%(grr_response_server/databases/mysql_migrations@"
    "grr-response-server|resource)", "Folder with MySQL migrations files.")

# Support for MySQL SSL connections.

config_lib.DEFINE_string(
    "Mysql.client_key_path",
    default="",
    help="The path name of the client private key file.")

config_lib.DEFINE_string(
    "Mysql.client_cert_path",
    default="",
    help="The path name of the client public key certificate file.")

config_lib.DEFINE_string(
    "Mysql.ca_cert_path",
    default="",
    help="The path name of the Certificate Authority (CA) certificate file. "
    "This option, if used, must specify the same certificate used by the "
    "server.")

# Legacy MySQLAdvancedDataStore used as AFF4 backend.
config_lib.DEFINE_string(
    "Mysql.database_name",
    default="grr",
    help="Name of the database to use for legacy MySQL-AFF4.")

config_lib.DEFINE_string(
    "Mysql.table_name",
    default="aff4",
    help="Name of the table to use for legacy MySQL-AFF4.")

config_lib.DEFINE_string(
    "Mysql.database_username",
    default="root",
    help="The user to connect to the database for legacy MySQL-AFF4.")

config_lib.DEFINE_string(
    "Mysql.database_password",
    default="",
    help="The password to connect to the database for legacy MySQL-AFF4.")

config_lib.DEFINE_integer(
    "Mysql.conn_pool_min",
    5,
    help="The minimum number of open connections to keep"
    " available in the pool for legacy MySQL-AFF4.")

config_lib.DEFINE_integer(
    "Mysql.max_connect_wait",
    600,
    help="Total number of seconds we wait for a "
    "connection before failing (0 means we wait "
    "forever) for legacy MySQL-AFF4..")

config_lib.DEFINE_integer(
    "Mysql.max_query_size",
    8 * 1024 * 1024,
    help="Maximum query size (in bytes). Queries sent by GRR to MySQL "
    "may be slightly bigger than the specified maximum. This "
    "value has to be smaller than MySQL's max_allowed_packet "
    "configuration value (for legacy MySQL-AFF4).")

config_lib.DEFINE_integer(
    "Mysql.max_values_per_query",
    10000,
    help="Maximum number of subjects touched by a single query "
    "for legacy MySQL-AFF4.")

config_lib.DEFINE_integer(
    "Mysql.max_retries",
    10,
    help="Maximum number of retries (happens in case a query fails) "
    "for legacy MySQL-AFF4.")
