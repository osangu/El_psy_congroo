CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

create table tbl_user (
                          id       uuid not null DEFAULT uuid_generate_v4(),
                          name     varchar(5)  not null,
                          email    varchar(10) not null,
                          password char(60)    not null,
                          primary key (id)
);

create table tbl_post(
    id serial not null,
    user_id uuid not null,
    title varchar(30) not null,
    content text not null,
    primary key (id),
    foreign key (user_id) references tbl_user(id)
);
