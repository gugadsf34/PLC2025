**Autor:** Gustavo da Silva Faria, a108575

<img width="344" height="269" alt="pfp" src="https://github.com/user-attachments/assets/bf9861a2-9d1d-425b-a42d-b3e486f22931" />


# Pergunta
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

# Resposta

[analisador](analisador.py)

[tokens](tokens.json)

## Input
```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```


## Output
```
('COMMENT', '# DBPedia: obras de Chuck Berry', 1, (0, 31))
('NEWLINE', '\n', 1, (31, 32))
('NEWLINE', '\n', 1, (32, 33))
('SELECT', 'select', 1, (33, 39))
('VAR', '?nome', 1, (40, 45))
('VAR', '?desc', 1, (46, 51))
('WHERE', 'where', 1, (52, 57))
('BRACE_A', '{', 1, (58, 59))
('NEWLINE', '\n', 1, (59, 60))
('VAR', '?s', 1, (62, 64))
('IDEN', 'a', 1, (65, 66))
('NOME', 'dbo:MusicalArtist', 1, (67, 84))
('PONTO', '.', 1, (84, 85))
('NEWLINE', '\n', 1, (85, 86))
('VAR', '?s', 1, (88, 90))
('NOME', 'foaf:name', 1, (91, 100))
('STRING', '"Chuck Berry"@en', 1, (101, 117))
('PONTO', '.', 1, (118, 119))
('NEWLINE', '\n', 1, (119, 120))
('VAR', '?w', 1, (122, 124))
('NOME', 'dbo:artist', 1, (125, 135))
('VAR', '?s', 1, (136, 138))
('PONTO', '.', 1, (138, 139))
('NEWLINE', '\n', 1, (139, 140))
('VAR', '?w', 1, (142, 144))
('NOME', 'foaf:name', 1, (145, 154))
('VAR', '?nome', 1, (155, 160))
('PONTO', '.', 1, (160, 161))
('NEWLINE', '\n', 1, (161, 162))
('VAR', '?w', 1, (164, 166))
('NOME', 'dbo:abstract', 1, (167, 179))
('VAR', '?desc', 1, (180, 185))
('NEWLINE', '\n', 1, (185, 186))
('RBRACE_F', '}', 1, (186, 187))
('IDEN', 'LIMIT', 1, (188, 193))
('NUM', '1000', 1, (194, 198))
('NEWLINE', '\n', 1, (198, 199))
```
