from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from beasties_app.models import Enemy, Zombie, Amino_Acid_Name, Amino_Acid, Bodypart

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/beasties/login/')

@login_required
def index(request):
    return render_to_response('beasties/index.html', {})

@login_required    
def graveyard(request):
    enemy_list = Enemy.objects.all()[:4]
    
    # Create dictionary of variables to pass to site
    vars = {}
    vars['enemy_list'] = enemy_list
    return render_to_response('beasties/graveyard.html', vars, context_instance=RequestContext(request))


@login_required    
# https://docs.djangoproject.com/en/1.3/intro/tutorial04/
def lab(request):
    # Try to create dictionary of variables to pass to site
    try:
        enemy = Enemy.objects.get(pk=request.POST['enemy_id'])
        
        #TODO: Set Player's current enemy
        #player = request.user.something
        #player.current_enemy_id = enemy
        
        vars = {}
        vars['amino_acid_names'] = Amino_Acid_Name.objects.all()[:]
        vars['amino_acids'] = Amino_Acid.objects.all()[:]
        vars['bodyparts'] = Bodypart.objects.all()[:] # ['hands', 'horns', 'mouth', 'tail']
        vars['enemy'] = enemy
        vars['template_mapping'] = [[1,'a'],[2,'b'],[3,'c']]
        
    except (KeyError, Enemy.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('beasties/index.html', {
            'error_message': "Beast not found.  Going home.",
        }, context_instance=RequestContext(request))
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render_to_response('beasties/lab.html', vars, context_instance=RequestContext(request))
        
@login_required
def fight(request):
    #TODO: Create new zombie with phenotypes selected in lab screen
    # zombie = new Zombie entry
    # vars = {}
    # return render_to_response('beasties/fight.html', vars, context_instance=RequestContext(request))
    
    # Get current user's zombie
    user = request.user
    zombie = user.zombie_set.filter(built_flag=True, deceased_flag=False)[0]
    
    # Get current enemy 
    #TODO: this should be an instance of User_Enemy, not Enemy
    # Will need to change the UserProfile model
    enemy = user.get_profile().current_enemy 
    
    # Construct list of enemy's weaknesses
    enemy_weaknesses = [weakness for weakness in enemy.weakness.all()]
    
    # Construct list of zombie's strengths
    hand_strength = zombie.hand_phenotype.strong_against.all()[0]
    horn_strength = zombie.horn_phenotype.strong_against.all()[0]
    mouth_strength = zombie.mouth_phenotype.strong_against.all()[0]
    tail_strength = zombie.tail_phenotype.strong_against.all()[0]
    
    zombie_strengths = [hand_strength, horn_strength, mouth_strength, tail_strength]
    
    # Check to see if the zombie has enough phenotypes to defeat the enemy
    enemy_set = set(enemy_weaknesses)
    zombie_set = set(zombie_strengths)
    common_set = zombie_set.intersection(enemy_set)
    
    fight_outcome = []
    # Declare winner and loser
    if len(common_set) >= len(enemy_set): 
        # Zombie wins, update won_flag
        zombie.won_flag = True
        
        fight_outcome.append(enemy.win_message)
        fight_outcome.append("Way to go!")
        
        #TODO: Here we would update the User_Enemy flags
        
        
    else:
        # Zombie loses
        zombie.won_flag = False
        needed_phen_num = len(common_set) - len(enemy_set)
        
        fight_outcome.append("You lost the fight!")
        fight_outcome.append("You needed "+ needed_phen_num + "phenotypes strong against the monster")
        
        #TODO: Here we would update the User_Enemy flags
    
    # Create context for template rendering
    vars = {}
    vars['fight_outcome'] = fight_outcome
    vars['enemy'] = enemy
    vars['zombie'] = zombie
    
    return render_to_response('beasties/fight.html', vars, context_instance=RequestContext(request))
    
        
    
    