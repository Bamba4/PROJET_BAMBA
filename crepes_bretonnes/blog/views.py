from django.shortcuts import render
from blog.models import Article, Contact
from .forms import ContactForm, ArticleForm, NouveauContactForm


def addArticle(request):
  form = ArticleForm(request.POST or None)
  if form.is_valid():
    titre = form.cleaned_data['titre']
   # auteur = form.cleaned_data['auteur']
   # slug = form.cleaned_data['slug']
    contenu = form.cleaned_data['contenu']
    #categorie = form.cleaned_data['categorie']
  return render(request, 'blog/article.html', locals())


#def contact(request):
  # Construire le formulaire, soit avec les données postées,
  # soit vide si l'utilisateur accède pour la première fois
  # à la page.
  #form = ContactForm(request.POST or None)
  # Nous vérifions que les données envoyées sont valides
  # Cette méthode renvoie False s'il n'y a pas de données
  # dans le formulaire ou qu'il contient des erreurs.
  #if form.is_valid():
    # Ici nous pouvons traiter les données du formulaire
   # sujet = form.cleaned_data['sujet']
   # message = form.cleaned_data['message']
   # envoyeur = form.cleaned_data['envoyeur']
   # renvoi = form.cleaned_data['renvoi']

    # Nous pourrions ici envoyer l'e-mail grâce aux données
    # que nous venons de récupérer
   # envoi = True

  # Quoiqu'il arrive, on affiche la page du formulaire.
  #return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
  sauvegarde = False
  form = NouveauContactForm(request.POST or None, request.FILES)
  if form.is_valid():
    contact = Contact()
    contact.nom = form.cleaned_data["nom"]
    contact.adresse = form.cleaned_data["adresse"]
    contact.photo = form.cleaned_data["photo"]
    contact.save()
    sauvegarde = True

  return render(request, 'blog/contact.html', {
    'form': form,
    'sauvegarde': sauvegarde
  })


def voir_contact(request):
  return render(request, 'blog/voir_contact.html', {'contacts': Contact.objects.all()})
