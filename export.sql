--
-- Файл сгенерирован с помощью SQLiteStudio v3.2.1 в Вс май 26 17:15:25 2019
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: AppConnectDb_drugshopnet
CREATE TABLE "AppConnectDb_drugshopnet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nameNet" varchar(20) NOT NULL, "urlNet" varchar(127) NOT NULL, "town" varchar(10) NOT NULL, "pathNet" varchar(127) NOT NULL, "class_link" varchar(127) NOT NULL, "class_price" varchar(127) NOT NULL);
INSERT INTO AppConnectDb_drugshopnet (id, nameNet, urlNet, town, pathNet, class_link, class_price) VALUES (1, 'Planetazdorovo', 'https://apteka.planetazdorovo.ru', 'Perm', '"/search/?sort=CHEAP&q="', '"product-card__title"', '"product-card__price"');
INSERT INTO AppConnectDb_drugshopnet (id, nameNet, urlNet, town, pathNet, class_link, class_price) VALUES (2, 'OtSklada', 'https://apteka-ot-sklada.ru', 'Perm', '"/catalog?q="', '"catalog-list-item product product-type widget"', '"product-price"');

-- Таблица: AppConnectDb_mycookie
CREATE TABLE AppConnectDb_mycookie (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, cookie varchar (127) NOT NULL, idNet INTEGER REFERENCES AppConnectDb_drugshopnet (id) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE);
INSERT INTO AppConnectDb_mycookie (id, cookie, idNet) VALUES (1, '{"name": "city_id", "value": "599", "domain": ".planetazdorovo.ru"}', 1);
INSERT INTO AppConnectDb_mycookie (id, cookie, idNet) VALUES (2, '{"name": "city", "value": "%D0%9F%D0%B5%D1%80%D0%BC%D1%8C", "domain": ".planetazdorovo.ru"}', 1);
INSERT INTO AppConnectDb_mycookie (id, cookie, idNet) VALUES (3, '{"name": "city_xml", "value": "1", "domain": ".planetazdorovo.ru"}', 1);
INSERT INTO AppConnectDb_mycookie (id, cookie, idNet) VALUES (4, '{"name": "region", "value": "96", "domain": ".planetazdorovo.ru"}', 1);
INSERT INTO AppConnectDb_mycookie (id, cookie, idNet) VALUES (5, '{"name": "arrt_cityselect", "value": "41", "domain": ".apteka-ot-sklada.ru"}', 2);

-- Таблица: AppConnectDb_position
CREATE TABLE AppConnectDb_position (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, product varchar (50) NOT NULL, link varchar (127) NOT NULL, price integer, requ integer);

-- Таблица: AppConnectDb_search
CREATE TABLE AppConnectDb_search (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, name varchar (100) NOT NULL, requestNumber integer DEFAULT (0));
INSERT INTO AppConnectDb_search (id, name, requestNumber) VALUES (1402, 'drug', 0);

-- Таблица: auth_group
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

-- Таблица: auth_group_permissions
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Таблица: auth_permission
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (1, 1, 'add_logentry', 'Can add log entry');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (2, 1, 'change_logentry', 'Can change log entry');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (3, 1, 'delete_logentry', 'Can delete log entry');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (4, 1, 'view_logentry', 'Can view log entry');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (5, 2, 'add_permission', 'Can add permission');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (6, 2, 'change_permission', 'Can change permission');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (7, 2, 'delete_permission', 'Can delete permission');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (8, 2, 'view_permission', 'Can view permission');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (9, 3, 'add_group', 'Can add group');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (10, 3, 'change_group', 'Can change group');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (11, 3, 'delete_group', 'Can delete group');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (12, 3, 'view_group', 'Can view group');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (13, 4, 'add_user', 'Can add user');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (14, 4, 'change_user', 'Can change user');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (15, 4, 'delete_user', 'Can delete user');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (16, 4, 'view_user', 'Can view user');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (17, 5, 'add_contenttype', 'Can add content type');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (18, 5, 'change_contenttype', 'Can change content type');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (19, 5, 'delete_contenttype', 'Can delete content type');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (20, 5, 'view_contenttype', 'Can view content type');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (21, 6, 'add_session', 'Can add session');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (22, 6, 'change_session', 'Can change session');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (23, 6, 'delete_session', 'Can delete session');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (24, 6, 'view_session', 'Can view session');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (25, 7, 'add_connecttab', 'Can add connect tab');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (26, 7, 'change_connecttab', 'Can change connect tab');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (27, 7, 'delete_connecttab', 'Can delete connect tab');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (28, 7, 'view_connecttab', 'Can view connect tab');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (29, 8, 'add_drugshopnet', 'Can add drug shop net');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (30, 8, 'change_drugshopnet', 'Can change drug shop net');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (31, 8, 'delete_drugshopnet', 'Can delete drug shop net');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (32, 8, 'view_drugshopnet', 'Can view drug shop net');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (33, 9, 'add_mycookie', 'Can add my cookie');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (34, 9, 'change_mycookie', 'Can change my cookie');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (35, 9, 'delete_mycookie', 'Can delete my cookie');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (36, 9, 'view_mycookie', 'Can view my cookie');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (37, 10, 'add_position', 'Can add position');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (38, 10, 'change_position', 'Can change position');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (39, 10, 'delete_position', 'Can delete position');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (40, 10, 'view_position', 'Can view position');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (41, 11, 'add_person', 'Can add person');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (42, 11, 'change_person', 'Can change person');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (43, 11, 'delete_person', 'Can delete person');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (44, 11, 'view_person', 'Can view person');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (45, 12, 'add_search', 'Can add search');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (46, 12, 'change_search', 'Can change search');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (47, 12, 'delete_search', 'Can delete search');
INSERT INTO auth_permission (id, content_type_id, codename, name) VALUES (48, 12, 'view_search', 'Can view search');

-- Таблица: auth_user
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);

-- Таблица: auth_user_groups
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Таблица: auth_user_user_permissions
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Таблица: django_admin_log
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));

-- Таблица: django_content_type
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO django_content_type (id, app_label, model) VALUES (7, 'AppConnectDb', 'connecttab');
INSERT INTO django_content_type (id, app_label, model) VALUES (8, 'AppConnectDb', 'drugshopnet');
INSERT INTO django_content_type (id, app_label, model) VALUES (9, 'AppConnectDb', 'mycookie');
INSERT INTO django_content_type (id, app_label, model) VALUES (10, 'AppConnectDb', 'position');
INSERT INTO django_content_type (id, app_label, model) VALUES (11, 'AppConnectDb', 'person');
INSERT INTO django_content_type (id, app_label, model) VALUES (12, 'AppConnectDb', 'search');

-- Таблица: django_migrations
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations (id, app, name, applied) VALUES (1, 'AppConnectDb', '0001_initial', '2019-05-01 10:43:47.147199');
INSERT INTO django_migrations (id, app, name, applied) VALUES (2, 'contenttypes', '0001_initial', '2019-05-01 10:43:47.296421');
INSERT INTO django_migrations (id, app, name, applied) VALUES (3, 'auth', '0001_initial', '2019-05-01 10:43:47.447018');
INSERT INTO django_migrations (id, app, name, applied) VALUES (4, 'admin', '0001_initial', '2019-05-01 10:43:47.556442');
INSERT INTO django_migrations (id, app, name, applied) VALUES (5, 'admin', '0002_logentry_remove_auto_add', '2019-05-01 10:43:47.676311');
INSERT INTO django_migrations (id, app, name, applied) VALUES (6, 'admin', '0003_logentry_add_action_flag_choices', '2019-05-01 10:43:47.787664');
INSERT INTO django_migrations (id, app, name, applied) VALUES (7, 'contenttypes', '0002_remove_content_type_name', '2019-05-01 10:43:47.940406');
INSERT INTO django_migrations (id, app, name, applied) VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2019-05-01 10:43:48.032800');
INSERT INTO django_migrations (id, app, name, applied) VALUES (9, 'auth', '0003_alter_user_email_max_length', '2019-05-01 10:43:48.122424');
INSERT INTO django_migrations (id, app, name, applied) VALUES (10, 'auth', '0004_alter_user_username_opts', '2019-05-01 10:43:48.222157');
INSERT INTO django_migrations (id, app, name, applied) VALUES (11, 'auth', '0005_alter_user_last_login_null', '2019-05-01 10:43:48.320894');
INSERT INTO django_migrations (id, app, name, applied) VALUES (12, 'auth', '0006_require_contenttypes_0002', '2019-05-01 10:43:48.410264');
INSERT INTO django_migrations (id, app, name, applied) VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2019-05-01 10:43:48.515487');
INSERT INTO django_migrations (id, app, name, applied) VALUES (14, 'auth', '0008_alter_user_username_max_length', '2019-05-01 10:43:48.605829');
INSERT INTO django_migrations (id, app, name, applied) VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2019-05-01 10:43:48.704562');
INSERT INTO django_migrations (id, app, name, applied) VALUES (16, 'auth', '0010_alter_group_name_max_length', '2019-05-01 10:43:48.820367');
INSERT INTO django_migrations (id, app, name, applied) VALUES (17, 'auth', '0011_update_proxy_permissions', '2019-05-01 10:43:48.917997');
INSERT INTO django_migrations (id, app, name, applied) VALUES (18, 'sessions', '0001_initial', '2019-05-01 10:43:49.010783');
INSERT INTO django_migrations (id, app, name, applied) VALUES (19, 'AppConnectDb', '0002_auto_20190501_1606', '2019-05-01 11:06:31.764928');
INSERT INTO django_migrations (id, app, name, applied) VALUES (20, 'AppConnectDb', '0003_remove_mycookie_namenet', '2019-05-01 11:17:48.927375');
INSERT INTO django_migrations (id, app, name, applied) VALUES (21, 'AppConnectDb', '0004_delete_connecttab', '2019-05-04 12:43:51.914592');
INSERT INTO django_migrations (id, app, name, applied) VALUES (22, 'AppConnectDb', '0005_person', '2019-05-04 13:05:58.148398');
INSERT INTO django_migrations (id, app, name, applied) VALUES (23, 'AppConnectDb', '0006_auto_20190506_1310', '2019-05-06 08:11:08.333129');
INSERT INTO django_migrations (id, app, name, applied) VALUES (24, 'AppConnectDb', '0007_auto_20190512_1511', '2019-05-12 10:11:43.005729');
INSERT INTO django_migrations (id, app, name, applied) VALUES (25, 'AppConnectDb', '0008_auto_20190512_1602', '2019-05-12 11:02:21.671412');
INSERT INTO django_migrations (id, app, name, applied) VALUES (26, 'AppConnectDb', '0009_remove_position_price', '2019-05-12 12:16:50.268181');
INSERT INTO django_migrations (id, app, name, applied) VALUES (27, 'AppConnectDb', '0010_position_price', '2019-05-12 12:20:14.215453');
INSERT INTO django_migrations (id, app, name, applied) VALUES (28, 'AppConnectDb', '0011_position_requ', '2019-05-12 20:11:35.935510');
INSERT INTO django_migrations (id, app, name, applied) VALUES (29, 'AppConnectDb', '0012_remove_position_requ', '2019-05-12 21:05:11.384861');
INSERT INTO django_migrations (id, app, name, applied) VALUES (30, 'AppConnectDb', '0013_position_requ', '2019-05-12 21:07:16.975460');
INSERT INTO django_migrations (id, app, name, applied) VALUES (31, 'AppConnectDb', '0014_auto_20190515_1621', '2019-05-15 11:21:45.441081');
INSERT INTO django_migrations (id, app, name, applied) VALUES (32, 'AppConnectDb', '0015_search_requestnumder', '2019-05-16 12:31:30.033243');
INSERT INTO django_migrations (id, app, name, applied) VALUES (33, 'AppConnectDb', '0016_auto_20190516_1732', '2019-05-16 12:33:03.570310');
INSERT INTO django_migrations (id, app, name, applied) VALUES (34, 'AppConnectDb', '0017_drugshopnet_pathnet', '2019-05-18 20:18:32.222757');
INSERT INTO django_migrations (id, app, name, applied) VALUES (35, 'AppConnectDb', '0018_auto_20190520_0034', '2019-05-19 19:34:36.769732');

-- Таблица: django_session
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

-- Индекс: auth_group_permissions_group_id_b120cbf9
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");

-- Индекс: auth_group_permissions_group_id_permission_id_0cd325b0_uniq
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");

-- Индекс: auth_group_permissions_permission_id_84c5c92e
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");

-- Индекс: auth_permission_content_type_id_2f476e4b
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");

-- Индекс: auth_permission_content_type_id_codename_01ab375a_uniq
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");

-- Индекс: auth_user_groups_group_id_97559544
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");

-- Индекс: auth_user_groups_user_id_6a12ed8b
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");

-- Индекс: auth_user_groups_user_id_group_id_94350c0c_uniq
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");

-- Индекс: auth_user_user_permissions_permission_id_1fbb5f2c
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");

-- Индекс: auth_user_user_permissions_user_id_a95ead1b
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");

-- Индекс: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");

-- Индекс: django_admin_log_content_type_id_c4bce8eb
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");

-- Индекс: django_admin_log_user_id_c564eba6
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");

-- Индекс: django_content_type_app_label_model_76bd3d3b_uniq
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");

-- Индекс: django_session_expire_date_a5c62663
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
