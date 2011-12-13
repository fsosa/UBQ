from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from beasties_app.models import Enemy, Amino_Acid_Name, Amino_Acid, Bodypart, Phenotype
from random import choice

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
    user = request.user
    
    DISPLAYABLE_ENEMIES = 4
    all_enemies = Enemy.objects.all()[:]
    enemy_list = []
    
    user_level = 1 #TODO user.get_profile().level
    defeated_enemies = eval('['+user.get_profile().defeated_enemies+']')
    #Check if player has less than 4 DISPLAYABLE_ENEMIES
    while(len(enemy_list) < 4):
        enemy = choice(all_enemies)
        
        if( enemy.group_number <= user_level and not (enemy in enemy_list) and not(enemy.id in defeated_enemies) ):
            enemy_list.append(enemy)
    
    # Create dictionary of variables to pass to site
    vars = {}
    vars['enemy_list'] = enemy_list
    
    enemies_weaknesses = {}
    for enemy in enemy_list:
        enemy_weaknesses = [enemy.weakness_1, enemy.weakness_2, enemy.weakness_3, enemy.weakness_4]
        enemy_weaknesses = filter (lambda weakness: weakness != None, enemy_weaknesses)
        weakness_count = {}
        for weakness in set(enemy_weaknesses):
            weakness_count[weakness] = enemy_weaknesses.count(weakness)
        enemies_weaknesses[enemy] = weakness_count
                    
    vars['enemies_weaknesses'] = enemies_weaknesses
    
    vars['user_wins'] = user.get_profile().win_count
    vars['user_losses'] = user.get_profile().loss_count
    
    return render_to_response('beasties/graveyard_accordian.html', vars, context_instance=RequestContext(request))


@login_required    
# https://docs.djangoproject.com/en/1.3/intro/tutorial04/
def lab(request):
    # Try to create dictionary of variables to pass to site
    vars = {}
    try:
        user = request.user 
        enemy = Enemy.objects.get(pk=request.POST['enemy_id'])

        vars['amino_acid_names'] = Amino_Acid_Name.objects.all()[:]
        vars['amino_acids'] = []
        #Get only unique amino acids
        for amino_acid_name in vars['amino_acid_names']:
            vars['amino_acids'].append(Amino_Acid.objects.filter(name=amino_acid_name.id)[0])
        
        vars['phenotypes'] = Phenotype.objects.all()[:]
        vars['bodyparts'] = Bodypart.objects.all()[:] # ['hands', 'horns', 'mouth', 'tail']
        vars['enemy'] = enemy
        
        enemy_weaknesses = [enemy.weakness_1, enemy.weakness_2, enemy.weakness_3, enemy.weakness_4]
        enemy_weaknesses = filter (lambda weakness: weakness != None, enemy_weaknesses)
        weakness_count = {}
        for weakness in set(enemy_weaknesses):
            weakness_count[weakness] = enemy_weaknesses.count(weakness)
            
        vars['weakness_count'] = weakness_count
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
# https://docs.djangoproject.com/en/1.3/intro/tutorial04/
def level2(request):
    # Try to create dictionary of variables to pass to site
    vars = {}
    try:
        enemy = Enemy.objects.get(pk=request.POST['enemy_id'])

        vars['amino_acid_names'] = Amino_Acid_Name.objects.all()[:]
        vars['amino_acids'] = Amino_Acid.objects.all()[:]
        vars['phenotypes'] = Phenotype.objects.all()[:]
        vars['bodyparts'] = Bodypart.objects.all()[:] # ['hands', 'horns', 'mouth', 'tail']
        vars['enemy'] = enemy
        
        enemy_weaknesses = [enemy.weakness_1, enemy.weakness_2, enemy.weakness_3, enemy.weakness_4]
        enemy_weaknesses = filter (lambda weakness: weakness != None, enemy_weaknesses)
        weakness_count = {}
        for weakness in set(enemy_weaknesses):
            weakness_count[weakness] = enemy_weaknesses.count(weakness)
            
        vars['weakness_count'] = weakness_count
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
        return render_to_response('beasties/level2.html', vars, context_instance=RequestContext(request))

        
@login_required
def fight(request):
    # Get current user and create the new zombie
    user = request.user 
    vars = {}
    fight_outcome = ""
    
    try:
        # Get chosen phenotypes from lab page
        hands = Phenotype.objects.get(name=request.POST['fight_hands'])
        horns = Phenotype.objects.get(name=request.POST['fight_horns'])
        mouth = Phenotype.objects.get(name=request.POST['fight_mouth'])
        tail  = Phenotype.objects.get(name=request.POST['fight_tail'])
        
        # Get current enemy 
        #TODO: this should be an instance of User_Enemy, not Enemy
        enemy = Enemy.objects.get(pk=request.POST['enemy_id'])
    except (KeyError, Phenotype.DoesNotExist):
        return render_to_response('beasties/index.html', {
            'error_message': "Phenotype not found.  Going home.",
        }, context_instance=RequestContext(request))
    except (KeyError, Enemy.DoesNotExist):
        
        return render_to_response('beasties/index.html', {
            'error_message': "Beast not found.  Going home.",
        }, context_instance=RequestContext(request))
    else:    
        vars['enemy'] = enemy
        
        # Construct list of enemy's weaknesses
        enemy_weaknesses = [enemy.weakness_1, enemy.weakness_2, enemy.weakness_3, enemy.weakness_4]
        enemy_weaknesses = filter (lambda weakness: weakness != None, enemy_weaknesses)
        
        # Construct list of zombie's strengths
        zombie_strengths = []
        zombie_strengths.extend(hands.strong_against.all())
        zombie_strengths.extend(horns.strong_against.all())
        zombie_strengths.extend(mouth.strong_against.all())
        zombie_strengths.extend(tail.strong_against.all())
        
        zombie_strengths = filter (lambda strength: strength != None, zombie_strengths)
        
        # Check to see if the zombie has enough phenotypes to defeat the enemy
        remaining_weaknesses = enemy_weaknesses
        for strength in zombie_strengths:
            if strength in enemy_weaknesses:
                remaining_weaknesses.remove(strength)
        
        # Declare winner and loser
        if len(remaining_weaknesses) == 0:
            # User wins
            user.get_profile().win_count += 1
            
            
            #Convert CharField to list and convert back to comma-separated after operation
            defeated_enemies = eval('['+user.get_profile().defeated_enemies+']')
            defeated_enemies.append(eval(request.POST['enemy_id']))
            defeated_str = str(defeated_enemies).strip('[').strip(']')
            
            user.get_profile().defeated_enemies = defeated_str
            user.get_profile().save()
            
            
            
            
            fight_outcome = "Way to go!  " + enemy.win_message
            
            
            vars['fight_outcome'] = fight_outcome
            return render_to_response('beasties/win_fight.html', vars, context_instance=RequestContext(request))
        else:
            # User loses
            user.get_profile().loss_count += 1
            user.get_profile().save()
            
            
            fight_outcome = "You lost the fight!  You needed another "
            
            weakness_count = {}
            for weakness in set(remaining_weaknesses):
                weakness_count[weakness.name] = remaining_weaknesses.count(weakness)
            
            for key in weakness_count:
                fight_outcome += str(weakness_count[key]) + " phenotype(s) against " + key
            vars['fight_outcome'] = fight_outcome
            
            
        
            # # Finalize changes to zombie
            # # Create context for template rendering
            
            return render_to_response('beasties/lose_fight.html', vars, context_instance=RequestContext(request))