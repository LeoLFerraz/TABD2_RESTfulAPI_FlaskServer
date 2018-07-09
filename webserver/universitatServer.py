from flask import Flask, send_from_directory, request, url_for, request, render_template
RESTAPIServer = Flask(__name__, static_url_path="", static_folder="") 
# I'm resetting flask's default static serving parameters 
# so that I can use my own architecture (config-based archi, as seen below)
# Still using send_from_directory for it's safety protocols (treatment of untrusted client input/url);

# CONFIGS/CONSTANTS
RESTAPIServer.config.update(
    PROJECTNAME='universitat',
    DEBUG=True,
    STATIC_PATH='./static',
    TEMPLATES_STATIC_PATH='./templates',
    CSS_STATIC_PATH='./static/css',
    JS_STATIC_PATH='./static/js'
    # ideally, would have constants for:
    ## api path
    ## each of the resource's path
    ## template's rendered texts
)
# END CONFIGS/CONSTANTS

@RESTAPIServer.route('/')
def serveIndex():
    print(request) #Debugging;
    return render_template(RESTAPIServer.config['PROJECTNAME'] + '.html', Configs=RESTAPIServer.config)
    # The 'Configs' parameter is passed on to be used as access to the server constants, which are used in the pages' links and script srcs. 
    # Flask's web server's static-content-serving-abstraction layer is weird :(
    # Forces me to get parameters from the server, rather than scrape the HTTP request for pathnames and serve the files accordingly (e.g.: if file extension == .css, access static/css/ and serve filename)
    # Ideally, I would have a "singleton" @.route that managed the requests. Instead, I'm forced to let Flask take care of everything for me.
    
@RESTAPIServer.route('/api/')
@RESTAPIServer.route('/api')
def serveAPIIndex():
    return render_template(RESTAPIServer.config['PROJECTNAME'] + '-api-index.html', Configs=RESTAPIServer.config)
    
# EXERCÍCIO 6: IMPLEMENTE SERVIÇO PARA CRIAR PESQUISADOR
@RESTAPIServer.route('/api/pesquisadores', methods=['PUT', 'POST'])
def safeCreateNewResearcher():
    # If method == PUT
    # Check if researcher exists, handle error
    # Else
    # Call createResearcher() from researcherDAO.
    # If method == POST
    # Check if researcher exists, call updateResearcher() from researcherDAO.
    # Else
    # Call createResearcher() from researcherDAO.
    return 'WIP' # return the response in JSON
# FIM EXERCÍCIO 6
    
# EXERCÍCIO 7: IMPLEMENTE SERVIÇO PARA CRIAR PROJETO DE PESQUISA
@RESTAPIServer.route('/api/projetos', methods=['PUT', 'POST'])
def safeCreateNewProject():
    # If method == PUT
    # Check if project exists, handle error
    # Else
    # Call createProject() from projectDAO.
    # If method == POST
    # Check is project exists, call updateProject() from projectDAO.
    # Else
    # Call createProject() from projectDAO.
    return 'WIP' # return the response in JSON
# FIM EXERCÍCIO 7

# EXERCÍCIO 8: IMPLEMENTE SERVIÇO PARA INICIAR PROJETO DE PESQUISA
@RESTAPIServer.route('/api/projetos/<int:id_project>/status', methods=['POST'])
def safeUpdateProjectStatus(id_project):
    # Check if project exists
    # If curStatus is == to newStatus, handle
    # If curStatus is cancelled, handle (can't change from cancelled)
    # if newStatus is within curStatus.allowedStatusUpdate (this is redundant with the previous conditions, but we use them anyway for their output) 
        # if newStatus is 'Em Andamento', call updateProject() changing status and start_date
        # if newStatus is 'Concluida', call updateProject() changing status and finish_date
        # Else
        # call updateProject() changing the status attribute
    # Else
    # Handle generic not allowed error.
    return 'WIP' # return the response in JSON
# FIM EXERCÍCIO 8

# EXERCÍCIO 9: IMPLEMENTE SERVIÇO PARA CANCELAR PROJETO
    # A estrutura do exercício 8 já atende essa demanda.
# FIM EXERCÍCIO 9

# EXERCÍCIO 10: IMPLEMENTE SERVIÇO PARA CONCLUIR PROJETO
    # A estrutura do exercício 9 já atende essa demanda.
# FIM EXERCÍCIO 10

# EXERCÍCIO 11: IMPLEMENTE SERVIÇO PARA ASSOCIAR PESQUISADORES A PROJETOS
@RESTAPIServer.route('/api/projetos/<int:id_project>/pesquisadores-vinculados', methods=['POST', 'PUT'])
def safeAssociateNewResearcher(id_project):
    # Check if project exists
    # Check if researcher exists
    # Check if researcher is not already associated
    # Check if researcher is not project's lead
    # If all above are true, call createResearcherProjectAssociation() from researcherProjectAssociationsDAO.
    return 'WIP' # return the response in JSON

@RESTAPIServer.route('/api/pesquisadores/<int:id_researcher>/projetos-participados', methods=['POST', 'PUT'])
def safeAssociateNewProject(id_researcher):
    # Check if project exists
    # Check if researcher exists
    # Check if researcher is not already associated
    # Check if researcher is not project's lead
    # If all above are true, call createResearcherProjectAssociation() from researcherProjectAssociationsDAO.
    return 'WIP' # return the response in JSON
# FIM EXERCÍCIO 11

# EXERCÍCIO 12: IMPLEMENTE SUMÁRIO EXECUTIVO
@RESTAPIServer.route('/api/projetos/<int:id_project>/sumario-executivo', methods=['GET'])
def returnProjectExecutiveSummary(id_project):
    # Check if project exists
    # Store in projectInfoJSON all project information serialized to a JSON object
    return render_template("executive-summary.html", Configs=RESTAPIServer.config#, projectInfo=projectInfoJSON
                          )

RESTAPIServer.run()