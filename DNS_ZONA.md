# Zona DNS insiel.com.br

## Antes (Central Server, NS dns1–4.insiel.com.br) — levantamento de 30/09/2026
| Nome | Tipo | Valor |
|---|---|---|
| @ | A | 177.101.144.108 (site antigo) |
| www | CNAME | insiel.com.br |
| @ | MX 0 | mx.insiel.com.br |
| mx | CNAME | mx.hospedagemweb.net |
| mail | CNAME | mail.hospedagemweb.net |
| smtp | CNAME | smtp.hospedagemweb.net |
| pop | CNAME | pop.hospedagemweb.net |
| pop3 | CNAME | pop3.hospedagemweb.net |
| webmail | CNAME | webmail.hospedagemweb.net |
| painel | CNAME | painel.plat.hospedagemweb.net |
| ftp | A | 177.101.144.108 |
| @ | TXT | v=spf1 include:_spf.hospedagemweb.net -all |
| default._domainkey | TXT | k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtdZmHUNeWF2m/twXdHKmW2gOQq9C+OyXjBjrm9DZ3QXOrDZdptnvXt65H0c05RTKhpfp+sZtjT7iBhw0mAuKp1HjeVYNegsQRgTkiB9ht2RXR8ESsHBfwe3p8s0dMiTHtcclDdJKPRRJnMkOlRC3FTBUqyDauK4K295PzeVbfZwIDAQAB |
| ns1 / ns2 | A | 186.233.144.22 / 186.233.145.22 (não usados na delegação) |
| dns1..dns4 | A (glue) | 177.101.144.23 / 186.233.144.25 / 177.101.144.22 / 177.101.144.25 |

Sem registros: AAAA, CAA, _dmarc, imap, autodiscover, autoconfig.

## Depois (zona no Registro.br, modo avançado) — o que deve existir
Mesma tabela acima, trocando só:
| @ | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (GitHub Pages) |
| www | CNAME | juanpinheiro1.github.io |
Todos os registros de e-mail (MX, mx, mail, smtp, pop, pop3, webmail, painel, SPF, DKIM) recriados idênticos.
