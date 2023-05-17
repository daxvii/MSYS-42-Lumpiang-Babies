DELETE FROM users; 
DELETE FROM groups;
DELETE FROM products;
DELETE FROM daily_orders;
DELETE FROM combos;
DELETE FROM components;
DELETE FROM inventory_records;

ALTER TABLE product AUTO_INCREMENT=1;
ALTER TABLE daily_order AUTO_INCREMENT=1;

INSERT INTO product
VALUES (1, 'Pork Shanghai Rolls', 75, 100, 20, 4, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (2, 'Bangus Relleno Rolls', 85, 100, 15, 3, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (3, 'Chicken Cordon Bleu Rolls', 85, 100, 10, 2, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (4, 'Beef Taco Rolls', 90, 100, 20, 4, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (5, 'Longganisa Rolls', 75, 100, 20, 4, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (6, 'Tuna Ala King Rolls', 85, 100, 10, 3, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (7, 'Cheese Samosa', 65, 100, 20, 2, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (8, 'Vegetable Spring Rolls', 75, 100, 15, 3, 'A-la-carte Lumpia', 'pieces');

INSERT INTO product
VALUES (9, 'Bottled Water', 20, 100, 30, 1, 'Drinks', 'bottles');

INSERT INTO product
VALUES (10, 'Lemon Iced Tea', 25, 100, 25, 1, 'Drinks', 'bottles');

-- INSERT INTO inventory
-- VALUES (1, 'Pork Shanghai Rolls', '2023-04-03', 100, 0, '', 20);

-- INSERT INTO inventory
-- VALUES (2, 'Bangus Relleno Rolls', '2023-04-03', 100, 0, '', 15);

-- INSERT INTO inventory
-- VALUES (3, 'Chicken Cordon Bleu Rolls', '2023-04-03', 100, 0, '', 10);

-- INSERT INTO inventory
-- VALUES (4, 'Beef Taco Rolls', '2023-04-03', 100, 0, '', 20);

-- INSERT INTO inventory
-- VALUES (5, 'Longganisa Rolls', '2023-04-03', 100, 0, '', 20);

-- INSERT INTO inventory
-- VALUES (6, 'Tuna Ala King Rolls', '2023-04-03', 100, 0, '', 10);

-- INSERT INTO inventory
-- VALUES (7, 'Cheese Samosa', '2023-04-03', 100, 0, '', 20);

-- INSERT INTO inventory
-- VALUES (8, 'Vegetable Spring Rolls', '2023-04-03', 100, 0, '', 15);

-- INSERT INTO inventory
-- VALUES (9, 'Bottled Water', '2023-04-03', 100, 0, '', 30);

-- INSERT INTO inventory
-- VALUES (10, 'Lemon Iced Tea', '2023-04-03', 100, 0, '', 25);