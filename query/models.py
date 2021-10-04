from django.db import models


class Deptno(models.Model):
	deptno = models.IntegerField(primary_key=True)
	dname  = models.CharField(max_length=30)
	loc    = models.CharField(max_length=20)
class Emp(models.Model):
	empno = models.IntegerField(primary_key=True,unique=True)
	ename = models.CharField( max_length=50)
	job = models.CharField( max_length=50)
	manager = models.CharField( blank=True,max_length=50,null=True)
	hiredate = models.DateField(null=True)
	sal      =models.IntegerField()
	cmm = models.IntegerField(blank=True,null=True)
	deptno = models.ForeignKey('Deptno',on_delete=models.CASCADE)

class Emp1(models.Model):
	empno = models.IntegerField(primary_key=True,unique=True)
	ename = models.CharField( max_length=50)
	job = models.CharField( max_length=50)
	manager = models.CharField( blank=True,max_length=50,null=True)
	hiredate = models.DateField(null=True)
	sal      =models.IntegerField()
	cmm = models.IntegerField(blank=True,null=True)
	deptno = models.ForeignKey('Deptno',on_delete=models.CASCADE)