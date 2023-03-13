DELETE FROM user_t;
DELETE FROM product;
DELETE FROM combo;
DELETE FROM daily_order;
DELETE FROM inventory;
DELETE FROM components;

INSERT INTO product
VALUES (1, 'Pork Shanghai Rolls', 75, 20, 4, '', 'pieces');

INSERT INTO product
VALUES (2, 'Bangus Relleno Rolls', 85, 15, 3, '', 'pieces');

INSERT INTO product
VALUES (3, 'Chicken Cordon Bleu Rolls', 85, 10, 2, '', 'pieces');

INSERT INTO product
VALUES (4, 'Beef Taco Rolls', 90, 20, 4, '', 'pieces');

INSERT INTO product
VALUES (5, 'Longganisa Rolls', 75, 20, 4, '', 'pieces');

INSERT INTO product
VALUES (6, 'Tuna Ala King Rolls', 85, 10, 3, '', 'pieces');

INSERT INTO product
VALUES (7, 'Cheese Samosa', 65, 20, 2, '', 'pieces');

INSERT INTO product
VALUES (8, 'Vegetable Spring Rolls', 75, 15, 3, '', 'pieces');

INSERT INTO product
VALUES (9, 'Bottled Water', 20, 30, 1, '', 'bottles');

INSERT INTO product
VALUES (10, 'Lemon Iced Tea', 25, 25, 1, '', 'bottles');