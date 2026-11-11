-- PMR3304 - Segunda entrega de laboratório - Parte 4: Exercícios com SQL
-- Banco: db.sqlite3 do projeto (tabelas criadas pelo Django)
--   blog_post(id, title, content, pub_date)
--   blog_comment(id, text, pub_date, author_id, post_id)
--   blog_category(id, name, description)
--   blog_post_categories(id, post_id, category_id)  <- tabela intermediária do N para N

-- 1. Todos os posts, ordenados pela data, sendo o mais recente primeiro
SELECT * FROM blog_post
ORDER BY pub_date DESC;

-- 2. Para um post com comentários (id = 3), todos os seus comentários
SELECT * FROM blog_comment
WHERE post_id = 3;

-- 3. Para um post com comentários (id = 3), todos os seus comentários, com todas
--    as colunas da tabela de comentários (exceto post_id), o título do post e
--    a sua data de publicação renomeada para post_date
SELECT c.id, c.text, c.pub_date, c.author_id, p.title, p.pub_date AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON c.post_id = p.id
WHERE c.post_id = 3;

-- 4. Para uma categoria (id = 2, "WEC"), todos os posts pertencentes a
--    ela, com as colunas da tabela de categoria e da tabela de posts
SELECT cat.*, p.*
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
JOIN blog_post AS p ON pc.post_id = p.id
WHERE cat.id = 2;

-- 5. Todas as categorias que possuem dois ou mais posts
SELECT cat.id, cat.name, COUNT(pc.post_id) AS posts_count
FROM blog_category AS cat
JOIN blog_post_categories AS pc ON pc.category_id = cat.id
GROUP BY cat.id
HAVING COUNT(pc.post_id) >= 2;
