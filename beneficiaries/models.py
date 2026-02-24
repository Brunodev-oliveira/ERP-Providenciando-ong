from django.db import models


class Beneficiary(models.Model):
    
    class Status(models.TextChoices):
        ACTIVE = "active", "Ativo"
        PENDING = "pending", "Pendente"
        SUSPENDED = "suspended", "Suspenso"
    

  
    class CivilStatus(models.TextChoices):
        SINGLE = "single", "Solteiro(a)"
        MARRIED = "married", "Casado(a)"
        DIVORCED = "divorced", "Divorciado(a)"
        SEPARATED = "separated", "Separado(a)"
        WIDOWED = "widowed", "Viúvo(a)"



    class Education(models.TextChoices):
        NO_FORMAL_EDUCATION = "no_formal_education", "Sem instrução formal"
        BASIC_LITERACY = "basic_literacy", "Alfabetizado (sem escolarização formal)"
        ELEMENTARY_INCOMPLETE = "elementary_incomplete", "Ensino Fundamental incompleto"
        ELEMENTARY_COMPLETE = "elementary_complete", "Ensino Fundamental completo"
        HIGH_SCHOOL_INCOMPLETE = "high_school_incomplete", "Ensino Médio incompleto"
        HIGH_SCHOOL_COMPLETE = "high_school_complete", "Ensino Médio completo"
        TECHNICAL = "technical", "Ensino Técnico (nível médio)"
        UNDERGRADUATE_INCOMPLETE = "undergraduate_incomplete", "Ensino Superior incompleto"
        UNDERGRADUATE_COMPLETE = "undergraduate_complete", "Ensino Superior completo"
        SPECIALIZATION = "specialization", "Pós-graduação (Especialização / MBA)"
        MASTERS = "masters", "Mestrado"
        DOCTORATE = "doctorate", "Doutorado"
        POSTDOCTORATE = "postdoctorate", "Pós-Doutorado"

    class ColorRace(models.TextChoices):
        BRANCA = "white", "Branca"
        PRETA = "black", "Preta"
        PARDA = "brown", "Parda"
        AMARELA = "asian", "Amarela"
        INDIGENA = "indigenous", "Indígena"



   
    class UF(models.TextChoices):
        AC = "AC", "Acre"
        AL = "AL", "Alagoas"
        AM = "AM", "Amazonas"
        AP = "AP", "Amapá"
        BA = "BA", "Bahia"
        CE = "CE", "Ceará"
        DF = "DF", "Distrito Federal"
        ES = "ES", "Espírito Santo"
        GO = "GO", "Goiás"
        MA = "MA", "Maranhão"
        MT = "MT", "Mato Grosso"
        MS = "MS", "Mato Grosso do Sul"
        MG = "MG", "Minas Gerais"
        PA = "PA", "Pará"
        PB = "PB", "Paraíba"
        PE = "PE", "Pernambuco"
        PI = "PI", "Piauí"
        PR = "PR", "Paraná"
        RJ = "RJ", "Rio de Janeiro"
        RN = "RN", "Rio Grande do Norte"
        RS = "RS", "Rio Grande do Sul"
        RO = "RO", "Rondônia"
        RR = "RR", "Roraima"
        SC = "SC", "Santa Catarina"
        SE = "SE", "Sergipe"
        SP = "SP", "São Paulo"
        TO = "TO", "Tocantins"

    id_beneficiary = models.AutoField(primary_key=True)
    beneficiary_name = models.CharField(max_length=200,verbose_name="Nome Completo")
    birth_date = models.DateField(verbose_name="Data de nascimento")
    cpf = models.CharField(max_length=14,unique=True, blank=False, null=False,)
    zip_code = models.CharField(max_length=9,blank=False,null=False,verbose_name="CEP")
    street = models.CharField(max_length=200, blank=False, null=False, verbose_name="Rua")
    address_number = models.IntegerField(blank=False,null=False,verbose_name="Número") 
    address_complement = models.CharField(max_length=50, blank=True,null=True,verbose_name="Complemento")
    neighborhood = models.CharField(max_length=100,blank=False,null=False,verbose_name="Bairro")
    community_name = models.CharField(max_length=30,blank=True,null=False,verbose_name="Nome da comunidade" ) 
    city = models.CharField(max_length=100,blank=False,null=False,verbose_name="Cidade")
    state = models.CharField(max_length=2, choices=UF.choices,blank=False, null=False,verbose_name="UF")
    phone = models.CharField(max_length=15,blank=False,null=False,verbose_name="Telefone")
    email = models.EmailField(blank=False,null=False,verbose_name="E-mail")
    education = models.CharField(max_length=50, null=False,blank=False, choices=Education.choices,default='no_formal_education', verbose_name="Escolaridade")
    occupation = models.CharField(max_length=100, verbose_name="Profissão")
    race= models.CharField(max_length=20,blank=True,null=True, choices=ColorRace.choices, verbose_name="Cor/Raça")
    civil_status = models.CharField(max_length=30, choices=CivilStatus.choices,blank=False,null=False,default='single', verbose_name="Estado Civil")
    family_income = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Renda Familiar")
    dependents_count = models.IntegerField(default=0,blank=True,null=True, verbose_name="Nº dependentes")
    household_members = models.IntegerField(blank=False,null=False,verbose_name="Nº de pessoas da Família")
    emergency_contact = models.JSONField(blank=True, null=True, verbose_name="Contatos de Emergência")
    status = models.CharField(max_length=10,choices=Status.choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data do Registro")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ultima atualização")

    projects = models.ManyToManyField('projects.Project', through='projects.Enrollment')


    

    def __str__(self):
        return self.beneficiary_name
    
    class Meta:
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'