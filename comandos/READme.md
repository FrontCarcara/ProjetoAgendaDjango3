Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
Configurar o git
python manage.py startapp contact

git config --global user.name 'Frontelli'
git config --global user.email 'matheusfrontelli@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git push
git remote add origin https://github.com/FrontCarcara/ProjetoAgendaDjango2.git
git reset <arquivo>

Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME




Configurar na base de dados pelo Django Shell

python manage.py shell
>>> from contact.models import Contact
>>> Contact
<class 'contact.models.Contact'>
>>> c = Contact(first_name = 'Gustavo') 
>>> c
<Contact: Gustavo >
>>> c.save()
c.last_name = 'Moreira'
c.delete
c  = Contact.objects.get(id=1) 
> c  = Contact.objects.get(pk=1)
>>> c = Contact.objects.all() 
>>> for contato in c: contato.first_name
c = Contact.objects.filter(pk=1)
>>> c = Contact.objects.all().order_by('-id') 