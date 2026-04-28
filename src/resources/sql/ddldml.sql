create user 'firstcommit'@'%' identified by '1111';
grant all privileges on *.* to 'firstcommit'@'%';
show grants for 'firstcommit'@'%';

CREATE TABLE menu (
    menu_id VARCHAR(10) PRIMARY KEY,
    parent_id VARCHAR(10) NULL,
    menu_name VARCHAR(100) NOT NULL,
    sort_order INT DEFAULT 0,
    is_active CHAR(1) DEFAULT 'Y',

    CONSTRAINT fk_menu_parent
        FOREIGN KEY (parent_id)
        REFERENCES menu(menu_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;
-- =====================================================
-- 2. 화면 (screen)
-- =====================================================
CREATE TABLE screen (
    screen_id    varchar(10) PRIMARY KEY,
    screen_name  VARCHAR(100) NOT NULL,
    file_path    VARCHAR(255) NOT NULL,
    is_active    CHAR(1) DEFAULT 'Y'
) ENGINE=InnoDB;

-- =====================================================
-- 3. 메뉴-화면 매핑
-- =====================================================
CREATE TABLE menu_screen (
    menu_id    varchar(10) NOT NULL,
    screen_id  varchar(10) NOT NULL,

    PRIMARY KEY (menu_id),

    CONSTRAINT fk_menu_screen_menu
        FOREIGN KEY (menu_id)
        REFERENCES menu(menu_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_menu_screen_screen
        FOREIGN KEY (screen_id)
        REFERENCES screen(screen_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =====================================================
-- 4. 권한 테이블
-- =====================================================
CREATE TABLE role (
    role_id    varchar(10) PRIMARY KEY,
    role_name  VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- =====================================================
-- 5. 메뉴-권한 매핑
-- =====================================================
CREATE TABLE menu_role (
    menu_id  varchar(10) NOT NULL,
    role_id  varchar(10) NOT NULL,

    PRIMARY KEY (menu_id, role_id),

    CONSTRAINT fk_menu_role_menu
        FOREIGN KEY (menu_id)
        REFERENCES menu(menu_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_menu_role_role
        FOREIGN KEY (role_id)
        REFERENCES role(role_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

USE CUST_ANALYSIS;


INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0001000000',NULL, 'HOME',1,'Y',1);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002000000',NULL, '분석',2,'Y',1);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0003000000',NULL,'시스템',3,'Y',1);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002001000', '0002000000', '잠재고객',4,'Y',2);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002002000', '0002000000','기존고객',5,'Y',2);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0003001000', '0003000000', '웹크롤링',6,'Y',2);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002001001', '0002001000', '렌터카 FAQ 분석',7,'Y',3);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002001002', '0002001000', '자동차 등록 현황 분석',8,'Y',3);
INSERT INTO cust_analysis.menu (menu_id, parent_id, menu_name, sort_order, use_yn, depth) VALUES('0002002001', '0002002000', '자동차 사고 현황 분석',9,'Y',3);


USE cust_analysis;

show tables;               
select * from menu;

ALTER TABLE cust_analysis.screen
MODIFY COLUMN screen_id VARCHAR(30); -- 글자수가 17글자로 10글자를 넘어 오류가 발생함-> 해당 id만 글자 수를 늘려줌.

INSERT INTO cust_analysis.screen (screen_id, screen_name, file_path, use_yn) VALUES('car_acc.py', '자동차사고현황분석', 'src/views/analysis/new_cust','Y');
INSERT INTO cust_analysis.screen (screen_id, screen_name, file_path, use_yn) VALUES('car_reg.py', '자동차등록현황분석', 'src/views/analysis/old_cust','Y');
INSERT INTO cust_analysis.screen (screen_id, screen_name, file_path, use_yn) VALUES('rental_car_faq.py', '렌터카FAQ분석', 'src/views/analysis/old_cust','Y');
INSERT INTO cust_analysis.screen (screen_id, screen_name, file_path, use_yn) VALUES('home.py', '홈화면', 'src/views/home','Y');
INSERT INTO cust_analysis.screen (screen_id, screen_name, file_path, use_yn) VALUES('crawling.py', '웹크롤링', 'src/views/system/crawling','Y');

select * from screen;

INSERT INTO cust_analysis.role (role_id, role_name) VALUES('sys_admin', '시스템_관리자');
select * from role;