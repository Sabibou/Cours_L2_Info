<!-- 

CREATE TABLE DEPT
	(DEPTNO NUMBER(2) CONSTRAINT PK_DEPT PRIMARY KEY,
	DNAME VARCHAR2(14) ,
	LOC VARCHAR2(13));

CREATE TABLE EMP
	(EMPNO NUMBER(4) CONSTRAINT PK_EMP PRIMARY KEY,
	ENAME VARCHAR2(10),
	JOB VARCHAR2(9),
	MGR NUMBER(4),
	HIREDATE DATE,
	SAL NUMBER(7,2),
	COMM NUMBER(7,2),
	DEPTNO NUMBER(2) CONSTRAINT FK_DEPTNO REFERENCES DEPT);

CREATE TABLE SALS 
	(job varchar2(9), 
	lsal number(7,2), 
	hsal number(7,2));

-->

# Exercice 1

## Question 2.

> **Exécutez les commandes suivantes à partir de la Session 1 :**

```sql
INSERT INTO EMP VALUES (7000,'Petit Lion', 'SALESMAN',7902,to_date('17-12-1980','dd-mm-yyyy'),800,NULL,20);
INSERT INTO EMP VALUES (7001,'Chaussette','SALESMAN',7698,to_date('20-2-1981','dd-mm-yyyy'),1600,300,20);
```

## Question 3.

> **Retournez à la Session 2 et vérifiez si vos modifications sont visibles à partir de cette session. Que constatez-vous ?**

On peut vérifier avec la commande `SELECT * FROM EMP;` que les modifications ne sont pas visibles.

Les modifications ne sont pas visibles car on n'a pas fait de commit.

## Question 4.

> **A partir de la Session 1, faites un COMMIT des modifications et vérifiez si les modifications sont connues dans la Session 2.**

On peut vérifier avec la commande `SELECT * FROM EMP;` que les modifications sont visibles.

Cette fois-ci, les modifications sont visibles car on a fait un commit.

## Question 5.

> **A partir de la Session 1, augmenter le salaire de l’employé ‘petit lion’ de 200 Euros.**

On peut augmenter le salaire de l'employé 'petit lion' de 200 Euros avec la commande `UPDATE EMP SET SAL = SAL + 200 WHERE ENAME = 'Petit Lion';`.

## Question 6.

> **A partir de la Session 2, mettez le salaire de l’employé ‘petit lion’ à 700 Euros. Que se passe-t-il ?**

On peut mettre le salaire de l'employé 'petit lion' à 700 Euros avec la commande `UPDATE EMP SET SAL = 700 WHERE ENAME = 'Petit Lion';`.

Lorsque l'on fait cette commande, la base de données attend que l'on valide la modification de la session 1. On peut valider la modification avec la commande `COMMIT;`.

## Question 7.

> **Faites un COMMIT dans la Session 1. Que se passe-t-il ? Faites un select dans les 2 sessions pour voir la modification.** 

On fait un select avec la commande `SELECT * FROM EMP;` dans les 2 sessions pour voir la modification.

On a deux versions différentes de la table EMP. Dans la session 1, on a un prix à 1000 et dans la session 2, on a un prix à 700.

## Question 8.

> **Faites un COMMIT dans la deuxième session. Faites un select dans les 2 sessions pour voir la modification.**

Après le commit dans la deuxième session, on a un prix à 700 dans les deux sessions.

## Question 9.

> **Utilisez un `SELECT FOR UPDATE` sur la Session 1 et essayez de modifier le salaire des employés à partir de la Session 2.**

On applique la commande `SELECT * FROM EMP FOR UPDATE;` dans la session 1.

On essaye de modifier le salaire des employés à partir de la session 2 avec la commande `UPDATE EMP SET SAL = 700 WHERE ENAME = 'Petit Lion';`.

Comme tout à l'heure on est bloqué par la session 1.


# Exercice 2

> **Rappel : mode de fonctionnement par défaut d’Oracle**
> **— Les lectures ne bloquent ni les autres lectures ni les écritures.**
> **— Les lectures ne sont bloquées par rien, même pas par un blocage d’une table en mode exclusif.**
> **— Il n’y pas de lecture impropre.**
> **— Il n’y a pas de pertes de mises à jour.**
> **— Il peut y avoir des lectures non reproductibles.**
> **— Il peut y avoir des lignes fantômes.**

## Question 1.

> **Pour chacun des scénarios ci-dessous, exécuter la séquence d’instructions à partir de deux sessions (session 1 et session 2) et expliquer quels sont les phénomènes observés ?**

### a)

Scénario 1. :

```sql
select sal from emp where empno = 7369; -- session 1
update emp set sal= 802 where empno = 7369 ; -- session 2
COMMIT; -- session 2
select sal from emp where empno = 7369 ; -- session 1
```

On obtient :

```
1.
       SAL
----------
       800

2.
1 row updated.


3.
Commit complete.

4.
       SAL
----------
       802
```

On a d'abord demandé le salaire de l'employé 7369 dans la session 1. On a obtenu 800. Puis, on a modifié le salaire de l'employé 7369 dans la session 2. On a obtenu 802. Enfin, on a demandé le salaire de l'employé 7369 dans la session 1. On a obtenu 802. 

### b)

Scénario 2. :

```sql
update emp set sal= 801 where empno = 7369 ; -- session 1
select sal from emp where empno = 7369 ; -- session 2
commit ; -- session 1
select sal from emp where empno = 7369 ; -- session 2
```

On obtient :

```
1.
1 row updated.

2.
       SAL
----------
        802

3.
Commit complete.

4.
       SAL
----------
        801
```

On a d'abord modifié le salaire de l'employé 7369 dans la session 1. On a obtenu 801. Puis, on a demandé le salaire de l'employé 7369 dans la session 2. On a obtenu 802. Enfin, on a demandé le salaire de l'employé 7369 dans la session 2. On a obtenu 801.

### c)

Scénario 3. :

```sql
update emp set sal= 803 where empno = 7369 ; -- session 1
update emp set sal= 804 where empno = 7369 ; -- session 2
commit ; -- session 1
commit ; -- session 2
```

On obtient :

```
1.
1 row updated.

2.
[Attente de la session 1]

3.
Commit complete.

4.
Commit complete.
```

On regarde les valeurs avec la commande `SELECT * FROM EMP WHERE EMPNO = 7369;`. On obtient 804.

On a d'abord modifié le salaire de l'employé 7369 dans la session 1. On a obtenu 803. Puis, on a modifié le salaire de l'employé 7369 dans la session 2. On a obtenu 804. Enfin, on a fait un commit dans la session 1. On a obtenu 804.

### d)

Scénario 4. :

```sql
update emp set sal= 805 where empno = 7369 ; -- session 1
update emp set sal = 1301 where empno=7521 ; -- session 2
update emp set sal = 1302 where empno=7521 ; -- session 1
update emp set sal= 806 where empno = 7369 ; -- session 2
```

On obtient :

```
1.
1 row updated.

2.
1 row updated.

3.
[Attente de la session 2]

4.
ORA-00060: deadlock detected while waiting for resource (session 1)
[Attente de la session 1] (session 2)
```

On regarde les valeurs avec : `SELECT * FROM EMP WHERE EMPNO = 7369 OR EMPNO = 7521;`. On obtient 806 et 1301.

> **Attendre un peu et faire un `ROLLBACK` dans la session 1.**

On observe les valeurs avec : `SELECT * FROM EMP WHERE EMPNO = 7369 OR EMPNO = 7521;`. On obtient 805 et 1301.


# Exercice 3

## A) Empêcher les lectures non reproductibles

> **Que pouvez-vous faire pour empêcher les lectures non reproductibles, dans chacun des cas suivants :**
> — dans le cas où la transaction ne modifie aucune donnée.
> — dans le cas où elle modifie des données.

Si la transaction ne modifie aucune donnée, on peut utiliser la commande `SET TRANSACTION READ ONLY;` pour empêcher les lectures non reproductibles.

Si la transaction modifie des données, on peut utiliser la commande `SET TRANSACTION READ WRITE;` pour empêcher les lectures non reproductibles. Cela permet de bloquer les autres transactions qui essaient de modifier les données de la table.

## B) Empêcher les lignes fantômes

Mêmes questions que l’exercice précédent, mais pour les lignes fantômes.

### Read Only

#### Question 1.

> **Ouvrez une nouvelle transaction en "READ ONLY".**

On peut le faire avec la commande `SET TRANSACTION READ ONLY;`.

#### Question 2.

> **Ouvrez en parallèle une deuxième transaction dans laquelle vous modifiez les salaires des employés.**

Pour cela, on utilise la commande `UPDATE EMP SET SAL = 314 WHERE ENAME = 'Petit Lion';`.

#### Question 3.

> **Validez cette deuxième transaction. Voyez-vous les modifications dans la première tran- saction ?**

On valide avec la commande `COMMIT;`. On ne voit pas les modifications dans la première transaction (On peut le vérifier avec la commande `SELECT * FROM EMP WHERE ENAME = 'Petit Lion';`).

#### Question 4.

> **Essayez de modifier des données dans la première transaction.**

On peut essayer de modifier les données avec `UPDATE EMP SET SAL = 314 WHERE ENAME = 'Petit Lion';`. On obtient l'erreur `ORA-01456: may not perform insert/delete/update operation inside a READ ONLY transaction`.

#### Question 5.

> **Que se serait-il passé si la première transaction n’avait pas été en "READ ONLY"? Vérifiez-le après avoir terminé la première transaction.**

On aurait pu modifier les données dans la première transaction. On peut le vérifier avec la commande `UPDATE EMP SET SAL = 314 WHERE ENAME = 'Petit Lion';`. On obtient bien la modification des données.

### Mode serialisable

Essayez de faire cet exercice en devinant ce qui va se passer avant de lancer chaque commande.

#### Question 1.

> **Ouvrez 2 sessions de travail avec des transactions T1 et T2.**

#### Question 2.

> **Passez T1 en mode sérialisé.**

On peut le faire avec la commande `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`.

#### Question 3.

> **T1 affiche tous les noms et salaires des employés.**

On peut le faire avec la commande `SELECT ENAME, SAL FROM EMP;`.


#### Question 4.

> **T2 modifie le salaire de l’employé ’WARD’.**

On peut le faire avec la commande `UPDATE EMP SET SAL = 314 WHERE ENAME = 'WARD';`.

#### Question 5.

> **T1 affiche à nouveau tous les salaires. Quel salaire voit-il pour l’employé ’WARD’? Pourquoi ?**

On peut le faire avec la commande `SELECT ENAME, SAL FROM EMP;`. On obtient 1301 pour l'employé WARD. C'est parce que T1 a été configurée en mode sérialisable. Donc, T1 ne voit pas les modifications de T2.

#### Question 6.

> **T2 valide sa transaction.**

On applique `COMMIT;`.

#### Question 7.

> **T1 affiche à nouveau tous les salaires. Quel salaire voit-il pour l’employé ’WARD’? Pourquoi ?**

On affiche les salaires avec la commande `SELECT ENAME, SAL FROM EMP;`. On obtient 1301 pour l'employé WARD. C'est parce que T1 a été configurée en mode sérialisable. Donc, T1 ne voit pas les modifications de T2.

On a donc gardé le même résultat que la question 5.


#### Question 8.

> **T1 modifie le salaire de l’employé ’WARD’. Que se passe-t-il ? Pourquoi ?**

On peut le faire avec la commande `UPDATE EMP SET SAL = 314 WHERE ENAME = 'WARD';`. On obtient l'erreur `ORA-08177: can't serialize access for this transaction`. C'est parce que T1 a été configurée en mode sérialisable. Donc, T1 ne peut pas modifier les données de la table.

#### Question 9.

> **T1 modifie le salaire d’un autre employé. Que se passe-t-il ?**

On peut le faire avec la commande `UPDATE EMP SET SAL = 314 WHERE ENAME = 'Petit Lion';`. On obtient bien la modification des données.

### Conclusion

> **Voyez-vous une différence avec le mode par défaut d’Oracle ? Explications ?**

On peut voir une différence avec le mode par défaut d'Oracle. En effet, dans le mode par défaut d'Oracle, on peut modifier les données dans la première transaction. En revanche, dans le mode sérialisable, on ne peut pas modifier les données dans la première transaction. 

Cela est dû au fait que le mode sérialisable permet de bloquer les autres transactions qui essaient de modifier les données de la table. Cela permet d'éviter les lectures non reproductibles et les lignes fantômes.