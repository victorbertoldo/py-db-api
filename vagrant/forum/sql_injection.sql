-- para o codigo referente ao forumdb_pg1.py existe uma brecha de segurança, q permite executar sql injection
-- por exemplo, para deleção de todos os posts
-- basta adicionar o codigo abaixo no formulário.
'); delete from posts; --