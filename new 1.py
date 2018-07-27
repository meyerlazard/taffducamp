import cherrypy
class homepage(object):
	def _init_(self):
		self.maxime = maxime()
		self.liens = pagedeliens()
	def index(self):
		return '''
				<h3>site des adorateurs de python - page d'accueil. </h3>
				<p>Veuillez visiter nos rubriques : </p>
				<ul>
					<li><a href = "/entrenous">Restons entre nous </a></li>
					<li><a href = "/maxime">Un maxime subtile </a></li>
					<li><a href = "/liens/utile"> Des liens utiles </a></li>
				<ul>
			'''
	index.exposed = True
	def entrenous(self):
		return '''
				cette page est produite à la racine du site. <br/>
				[<a href ="/"> Retour </a>]
			'''
	entrenous.exposed = True

Class maxime(object):
	def index(self):
		return '''
				<h3> il existe 10 sortes de gens </h3>
				<p>[<a href ="../">Retour</a>]</p>
			'''
	index.exposed = True
	
Class pagedeliens(object):
	def _init_ (self):
		self.extra = lienssupp()
	def index(self):
		return '''
			<p> page de liens </p>
			<p> en fait les liens <a href = "utiles"> sont plutôt ici </a></p>
		'''
	index.exposed = True
	def utiles (self):
		return '''
				<p> Quelques liens utiles </p>
				<ul>
					<li><a href = "http://www.cherrypy.org"> site de cherrypy </a></li>
					<li><a href = "http://www.python.org"> Site de python</a></li>
				</ul>
				<p> d'autres liens utiles 
				<a href = "./extra/">ici </a>.</p>
				<p>[<a href = "../">Retour</a>]</p>
			'''
	utiles.exposed = True
	
Class liens (object):
	def index (self):
		return '''
			<p>Encore quelques instants </p>
			<ul>
				<li><a href = "http://pythomium.net">le site de l'auteur</a></li>
				<li><a href = "http://ubuntu-fr.org>Ubuntu : le must </a></li>
			</ul>
			<p>[<a href = "../">Retour à la page</a>]</p>
		'''
	index.exposed = True 
racine = homepage()

cherrypy.quickstart(racine)
