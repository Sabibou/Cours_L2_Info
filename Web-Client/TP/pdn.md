# Question 1

Réponse de la commande `curl -v https://lmbp.uca.fr/~barrel/tp1/test.html`

```
*   Trying 193.54.49.17:443...
* Connected to lmbp.uca.fr (193.54.49.17) port 443 (#0)
* ALPN: offers h2
* ALPN: offers http/1.1
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* (304) (OUT), TLS handshake, Client hello (1):
* (304) (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN: server did not agree on a protocol. Uses default.
* Server certificate:
*  subject: C=FR; ST=Auvergne-Rh�ne-Alpes; O=Universit� Clermont Auvergne; CN=lmbp.uca.fr
*  start date: May  4 00:00:00 2022 GMT
*  expire date: May  4 23:59:59 2023 GMT
*  subjectAltName: host "lmbp.uca.fr" matched cert's "lmbp.uca.fr"
*  issuer: C=NL; O=GEANT Vereniging; CN=GEANT OV RSA CA 4
*  SSL certificate verify ok.
> GET /~barrel/tp1/test.html HTTP/1.1
> Host: lmbp.uca.fr
> User-Agent: curl/7.86.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Wed, 01 Feb 2023 06:52:10 GMT
< Server: Apache
< Content-Location: test.html.txt.fr
< Vary: negotiate,accept,accept-language
< TCN: choice
< Last-Modified: Mon, 18 Mar 2019 06:24:32 GMT
< ETag: "a-584587109a800;52adcf361d500"
< Accept-Ranges: bytes
< Content-Length: 10
< Content-Type: text/plain
< Content-Language: fr
< 
Bienvenue
* Connection #0 to host lmbp.uca.fr left intact
```


# Question 2

On peut lister les méthodes autorisées en rajoutant `-X OPTIONS` à la commande `curl` :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Wed, 01 Feb 2023 07:12:12 GMT
< Server: Apache
< Vary: accept,accept-language
< Allow: GET,POST,OPTIONS,HEAD,TRACE
< Content-Length: 0
< Content-Type: text/plain
< Content-Language: fr
< 
* Connection #0 to host lmbp.uca.fr left intact
```

La ressource accepte les méthodes `GET`, `POST`, `OPTIONS`, `HEAD` et `TRACE`.

# Question 3

## Accept-Language

On rajoute `-H "Accept-Language: 'en-US, en; q=1'"` à la commande `curl` :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Wed, 01 Feb 2023 07:28:14 GMT
< Server: Apache
< Content-Location: test.html.txt.en
< Vary: negotiate,accept,accept-language
< TCN: choice
< Last-Modified: Mon, 18 Mar 2019 06:24:37 GMT
< ETag: "8-584587155f340;52adcf361d500"
< Accept-Ranges: bytes
< Content-Length: 8
< Content-Type: text/plain
< Content-Language: en
< 
Welcome
* Connection #0 to host lmbp.uca.fr left intact
```

Le coefficient `q` est le coefficient de qualité. Il permet de donner une priorité à une langue par rapport à une autre. Ici, on demande la ressource en anglais, mais si elle n'est pas disponible, on accepte le français.

## Content-Type

On change le content type avec `-H 'Accept: text/html'` :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Wed, 01 Feb 2023 07:48:21 GMT
< Server: Apache
< Content-Location: test.html.fr
< Vary: negotiate,accept,accept-language
< TCN: choice
< Last-Modified: Mon, 18 Mar 2019 06:24:45 GMT
< ETag: "7b-5845871d00540;52adcf361d500"
< Accept-Ranges: bytes
< Content-Length: 123
< Content-Type: text/html
< Content-Language: fr
< 
<!DOCTYPE html>
<html>
        <head>
        </head>

        <body>
                Bienvenue sur la page &eacute;crite en fran&ccedil;ais
        </body>
* Connection #0 to host lmbp.uca.fr left intact
</html>
```



# Question 4

On ajoute `If-Modified-Since: Mon, 18 Mar 2019 06:24:32 GMT` à la commande `curl` (équivalent à "Si le contenu a changé depuis la dernière fois que j'ai demandé cette ressource") :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 304 Not Modified
< Date: Wed, 01 Feb 2023 07:22:54 GMT
< Server: Apache
< ETag: "a-584587109a800;52adcf361d500"
< Content-Location: test.html.txt.fr
< Vary: negotiate,accept,accept-language
```

On ajoute `If-None-Match: "a-584587109a800;52adcf361d500"` à la commande `curl` (équivalent à "Si le contenu n'a pas changé depuis la dernière fois que j'ai demandé cette ressource") :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 304 Not Modified
< Date: Wed, 01 Feb 2023 07:26:07 GMT
< Server: Apache
< ETag: "a-584587109a800;52adcf361d500"
< Content-Location: test.html.txt.fr
< Vary: negotiate,accept,accept-language
< 
* Connection #0 to host lmbp.uca.fr left intact
```

# Question 5

On change l'`User-Agent` pour :

- Firefox 31.0 sous Windows
  - `curl -A "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0" https://lmbp.uca.fr/~barrel/tp1/page.php`
- Nitendo Switch
  - `curl -A "Mozilla/5.0 (Nintendo Switch; ShareApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.9 NintendoBrowser/5.1.0.13341" https://lmbp.uca.fr/~barrel/tp1/page.php`
- Playstation 4
  - `curl -A "Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)" https://lmbp.uca.fr/~barrel/tp1/page.php`


# Question 6

- Avec `curl https://lmbp.uca.fr/~barrel/tp1/ceciestuneerreur -v`, on provoque une erreur 404 car le lien n'existe pas, et que la ressource est statique :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Date: Wed, 01 Feb 2023 07:51:27 GMT
< Server: Apache
< Content-Length: 226
< Content-Type: text/html; charset=iso-8859-1
< 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /~barrel/tp1/ceciestuneerreur was not found on this server.</p>
</body></html>
* Connection #0 to host lmbp.uca.fr left intact
```

- Avec `https://www.malekal.com/wp-login.php?redirect_to=https%3А%2F%2Fwww.malekal.com%2Fwp-admin%2F&reauth=1`, on provoque une erreur 403 car on n'a pas les droits d'accès à la ressource :

```
* Connection state changed (MAX_CONCURRENT_STREAMS == 256)!
< HTTP/2 403 
< date: Wed, 01 Feb 2023 07:54:23 GMT
< content-type: text/plain; charset=UTF-8
< content-length: 16
< x-frame-options: SAMEORIGIN
< referrer-policy: same-origin
< cache-control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< expires: Thu, 01 Jan 1970 00:00:01 GMT
< set-cookie: __cf_bm=ip198NfXCFQ7Wt1iGH6PvwKXJgMl2AxzrQH_102oJI0-1675238063-0-AZsJLyHkEXHnCzgXruuz9g/ZizLn0/OUPoJF1VO80cAEsvvfzbs0Qb95ZtqKOdXq6kwXzwbekFPR/CUwXfjt7ik=; path=/; expires=Wed, 01-Feb-23 08:24:23 GMT; domain=.malekal.com; HttpOnly; Secure; SameSite=None
< strict-transport-security: max-age=15552000; includeSubDomains; preload
< x-content-type-options: nosniff
< server: cloudflare
< cf-ray: 79291e681facd702-CDG
< alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
< 
* Connection #0 to host www.malekal.com left intact
error code: 1020
```

- On provoque une erreur 406 avec `curl https://lmbp.uca.fr/~barrel/tp1/test.html -v -H "Accept: lol"` :

```
* Mark bundle as not supporting multiuse
< HTTP/1.1 406 Not Acceptable
< Date: Wed, 01 Feb 2023 08:10:28 GMT
< Server: Apache
< Alternates: {"test.html.de" 1 {type text/html} {language de} {length 80}}, {"test.html.en" 1 {type text/html} {language en} {length 79}}, {"test.html.fr" 1 {type text/html} {language fr} {length 123}}, {"test.html.txt.de" 1 {type text/plain} {language de} {length 11}}, {"test.html.txt.en" 1 {type text/plain} {language en} {length 8}}, {"test.html.txt.fr" 1 {type text/plain} {language fr} {length 10}}
< Vary: negotiate,accept,accept-language
< TCN: list
< Content-Length: 804
< Content-Type: text/html; charset=iso-8859-1
< 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>406 Not Acceptable</title>
</head><body>
<h1>Not Acceptable</h1>
<p>An appropriate representation of the requested resource /~barrel/tp1/test.html could not be found on this server.</p>
Available variants:
<ul>
<li><a href="test.html.de">test.html.de</a> , type text/html, language de</li>
<li><a href="test.html.en">test.html.en</a> , type text/html, language en</li>
<li><a href="test.html.fr">test.html.fr</a> , type text/html, language fr</li>
<li><a href="test.html.txt.de">test.html.txt.de</a> , type text/plain, language de</li>
<li><a href="test.html.txt.en">test.html.txt.en</a> , type text/plain, language en</li>
<li><a href="test.html.txt.fr">test.html.txt.fr</a> , type text/plain, language fr</li>
</ul>
</body></html>
* Connection #0 to host lmbp.uca.fr left intact
```

