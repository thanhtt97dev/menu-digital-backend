
-- Init data for Role table
INSERT INTO menu_digital.role
VALUES 
(1, 'admin'),
(2, 'shop_admin'),
(3, 'employee'),
(4, 'customer')

-- Init data for User table
INSERT INTO menu_digital.user (id, role_id, username, password, fullname, email, status)
VALUES 
('6de439c8-a27e-4c7a-b8b1-5d29b113b5f7', 1, NULL, NULL, 'Hiếu Lê Đức', 'leduchieu2001x@gmail.com', 1),
('6e4f3f7-6b75-4c36-a73a-5b93013da770', 3, NULL, NULL, 'Le Duc Hieu 02 (OMI.BU2)', 'hieuld02@ominext.com', 1);