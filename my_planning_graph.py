
from itertools import chain, combinations
from aimacode.planning import Action
from aimacode.utils import expr

from layers import BaseActionLayer, BaseLiteralLayer, makeNoOp, make_node

# my imports
from layers import ActionNode
#import io

class ActionLayer(BaseActionLayer):

    def _inconsistent_effects(self, actionA, actionB):
        """ Return True if an effect of one action negates an effect of the other

        See Also
        --------
        layers.ActionNode
        """
        # TODO: implement this function
        
        # check 'effect' vs 'effect'
        
        debug1 = False
        debug2 = False
        
        try:
            # test exception log by code error
            # aaa

            if debug1:
                MyHelper.log('function _inconsistent_effects()')
            
            for exprEffectA in actionA.effects:
    
                # Effect of Action A
                effectA = str(exprEffectA)
                
                # Not (Effect of Action A)
                notEffectA = MyHelper.strNegExpr(effectA)
                
                if debug1:
                    MyHelper.log('effectA='+effectA)
                    MyHelper.log('notEffectA='+notEffectA)
                                                        
                for exprEffectB in actionB.effects:
                    
                    # Effect of Action B
                    effectB = str(exprEffectB)
                    
                    # Not (Effect of Action B)
                    notEffectB = MyHelper.strNegExpr(effectB)
                    
                    if debug1:
                        MyHelper.log('effectB='+effectB)
                        MyHelper.log('notEffectB='+notEffectB)
                                    
                    if effectA == notEffectB or notEffectA == effectB:
                        if debug2:
                            MyHelper.log('Found mutex in _inconsistent_effects: ')
                            
                            MyHelper.log('actionA.effects = ' + str(actionA.effects))
                            MyHelper.log('actionA.expr = ' + str(actionA.expr))
                            MyHelper.log('actionB.effects = ' + str(actionB.effects))
                            MyHelper.log('actionB.expr = ' + str(actionB.expr))
                            
                            MyHelper.log('----------')
                        return True

        except Exception as ex:
            MyHelper.log_exception('Exception in _inconsistent_effects:', ex)
            return False
                
        return False


    def _interference(self, actionA, actionB):
        """ Return True if the effects of either action negate the preconditions of the other 
        
        See Also
        --------
        layers.ActionNode
        """
        # TODO: implement this function

        # check 'effect' vs 'precondition'
        
        debug1 = False
        debug2 = False
        
        try:
            
            # 1. Action A Effects vs Action B Precondition 
            for exprEffectA in actionA.effects:
    
                # Effect of Action A
                effectA = str(exprEffectA)
     
                # Not (Effect of Action A)
                notEffectA = MyHelper.strNegExpr(effectA)
     
                if debug1:
                    MyHelper.log('function _interference()')
                    MyHelper.log('effectA='+effectA)
                    MyHelper.log('notEffectA='+notEffectA)
                            
                for exprPreConB in actionB.preconditions:
    
                    # Precondition of Action B
                    preConB = str(exprPreConB)
    
                    # Not Precondition of Action B
                    notPreConB = MyHelper.strNegExpr(preConB)
                    
                    if debug1:
                        MyHelper.log('preConB='+preConB)
                        MyHelper.log('notPreConB='+notPreConB)
                    
                    # compare 
                    if effectA == notPreConB or notEffectA == preConB:
                        
                        if debug2:
                            MyHelper.log('Found mutex in _interference: ')
                            MyHelper.log('Action A Effects vs Action B Precondition')
                            
                            MyHelper.log('actionA.preconditions = ' + str(actionA.preconditions))
                            MyHelper.log('actionA.effects = ' + str(actionA.effects))
                            MyHelper.log('actionA.expr = ' + str(actionA.expr))
                            
                            MyHelper.log('actionB.preconditions = ' + str(actionB.preconditions))
                            MyHelper.log('actionB.effects = ' + str(actionB.effects))
                            MyHelper.log('actionB.expr = ' + str(actionB.expr))
                            
                            MyHelper.log('----------')
                        return True
                    
            # 2. Action B Effects vs Action A Precondition 
            for exprEffectB in actionB.effects:
    
                # Effect of Action B
                effectB = str(exprEffectB)
     
                # Not (Effect of Action B)
                notEffectB = MyHelper.strNegExpr(effectB)
     
                if debug1:
                    MyHelper.log('effectB='+effectB)
                    MyHelper.log('notEffectB='+notEffectB)
                            
                for exprPreConA in actionA.preconditions:
    
                    # Precondition of Action A
                    preConA = str(exprPreConA)
                    
                    # Not (Precondition of Action A)
                    notPreConA = MyHelper.strNegExpr(preConA)
                    
                    if debug1:
                        MyHelper.log('preConA='+preConA)
                        MyHelper.log('notPreConA='+notPreConA)
                    
                    # compare 
                    if effectB == notPreConA or notEffectB == preConA:
                        
                        if debug2:
                            MyHelper.log('Found mutex in _interference: ')
                            MyHelper.log('Action B Effects vs Action A Precondition')
                            
                            MyHelper.log('actionA.preconditions = ' + str(actionA.preconditions))
                            MyHelper.log('actionA.effects = ' + str(actionA.effects))
                            MyHelper.log('actionA.expr = ' + str(actionA.expr))
                            
                            MyHelper.log('actionB.preconditions = ' + str(actionB.preconditions))
                            MyHelper.log('actionB.effects = ' + str(actionB.effects))
                            MyHelper.log('actionB.expr = ' + str(actionB.expr))
                            
                            MyHelper.log('----------')
                        return True
                    
        except Exception as ex:
            MyHelper.log_exception('Exception in _interference:', ex)
            return False
        
        return False

    def _competing_needs(self, actionA, actionB):
        """ Return True if any preconditions of the two actions are pairwise mutex in the parent layer
        
        See Also
        --------
        layers.ActionNode
        layers.BaseLayer.parent_layer
        """
        # TODO: implement this function
        
        # check A parent layer 'precondition' vs B parent layer 'precondition'
                    
        debug1 = False
        debug2 = False
        
        try:
            
            if debug1:
                MyHelper.log('function _competing_needs()')
                MyHelper.log('actionA='+str(actionA))
                MyHelper.log('self.parent_layer='+str(self.parent_layer))
                MyHelper.log('self.parent_layer.parents='+str(self.parent_layer.parents))
                MyHelper.log('self.parent_layer.children='+str(self.parent_layer.children))
                
                # each layer have property __iter__ 
                # which allow direct looping layer object for its __store(items)
                for literal in self.parent_layer:
                    MyHelper.log('literal='+str(literal))    
                MyHelper.log('len(self.parent_layer)='+str(len(self.parent_layer)))
                MyHelper.log('----------')        
        
            for preA in actionA.preconditions:                      
                for preB in actionB.preconditions:
                    if self.parent_layer.is_mutex(preA, preB) or self.parent_layer.is_mutex(preB, preA):
    
                        if debug2:
                            MyHelper.log('Found mutex in _competing_needs: ')                    
                            MyHelper.log('actionA.preconditions = ' + str(actionA.preconditions))
                            MyHelper.log('actionA.expr = ' + str(actionA.expr))                    
                            MyHelper.log('actionB.preconditions = ' + str(actionB.preconditions))
                            MyHelper.log('actionB.expr = ' + str(actionB.expr))                    
                            MyHelper.log('----------')
    
                        return True
                    
        except Exception as ex:
            MyHelper.log_exception('Exception in _competing_needs:', ex)
            return False
        
        return False


class MyHelper():
    def log_clear(self):
        with open('logs.txt', 'w') as f:
            f.write('')
            f.close()
            
    def log(text):
        try:
            # a = append text
            with open('logs.txt', 'a') as f:
                f.write(str(text)+'\n')
                f.close()
        except Exception as ex:
            MyHelper.log_exception('Exception in MyHelper.log:', ex)
            
    def log_exception(heading, ex):
        MyHelper.log(heading)
        MyHelper.log('Type: '+str(type(ex)))
        MyHelper.log('Args: '+str(ex.args))
        MyHelper.log('Exception: '+str(ex))
        MyHelper.log('----------')
            
    def strNegExpr(expr):
        expr = str(expr)
        
        if expr[0] == '~':
            notExpr = str(expr[1:])
        else:
            notExpr = '~'+expr
            
        return notExpr
    
# testing helper class
#MyHelper.strNegExpr('have(cake)')
#MyHelper.strNegExpr('~have(cake)')
# works

class LiteralLayer(BaseLiteralLayer):
            
    def _inconsistent_support(self, literalA, literalB):
        """ Return True if all ways to achieve both literals are pairwise mutex in the parent layer

        See Also
        --------
        layers.BaseLayer.parent_layer
        """
        # TODO: implement this function
        
        # check all mutex of pairs of A parents and B parents

        debug1 = False
        debug2 = False
        
        try:
            
            if debug1:
                MyHelper.log('function _inconsistent_support()')
                MyHelper.log('type(literalA)='+str(type(literalA)))
                MyHelper.log('literalA='+str(literalA))
                MyHelper.log('type(literalB)='+str(type(literalB)))
                MyHelper.log('literalB='+str(literalB))
                MyHelper.log('self.parents='+str(self.parents))

                for item in self:
                    MyHelper.log('self.item='+str(item))
            
            # get a list of parents where effects (childrens) is literalA or literalB
            parent_list = []
            for parent_action in self.parent_layer:
                # parent_action is already an instance of class ActionNode
                # type(parent_action) is <class 'layers.ActionNode'>
                if literalA in parent_action.effects or literalB in parent_action.effects:
                    parent_list.append(parent_action)
                                    
            if debug2:
                if(len(parent_list) > 0):
                    MyHelper.log('literalA + literalB parent_list='+str(parent_list))
                        
            # logic
            #   if all mutex, return True
            #   if one pair is not mutex, return False
            is_pair_mutex = False
            for parentA in parent_list:
                for parentB in parent_list:
                    
                    if parentA == parentB:
                        continue
                    
                    is_pair_mutex = False

                    if self.parent_layer.is_mutex(parentA, parentB) or self.parent_layer.is_mutex(parentB, parentA):
                        if debug2:
                            MyHelper.log('Found mutex in _inconsistent_support: ')                    
                            MyHelper.log('parentA = ' + str(parentA))
                            MyHelper.log('parentB = ' + str(parentB))
                            MyHelper.log('----------')
        
                        is_pair_mutex = True
            
                    # if one pair is not mutex, return immediately to save processing time
                    if is_pair_mutex == False:
                        break
                
                # if one pair is not mutex, return immediately to save processing time
                if is_pair_mutex == False:
                    break
            
            # if all pairs are mutex, return True
            all_pairs_mutex = is_pair_mutex
            if all_pairs_mutex:
                return True
            else:
                return False
            
        except Exception as ex:
            MyHelper.log_exception('Exception in _inconsistent_support:', ex)
            return False
            
        return False

    def _negation(self, literalA, literalB):
        """ Return True if two literals are negations of each other """
        # TODO: implement this function

        # check A is ~B and B is ~A

        debug1 = False
        debug2 = False
        
        try:
            
            LiteralA = str(literalA)
            LiteralB = str(literalB)
            
            notLiteralA = MyHelper.strNegExpr(LiteralA)
            notLiteralB = MyHelper.strNegExpr(LiteralB)
    
            if debug1:
                MyHelper.log('function _negation()')
                MyHelper.log('LiteralA='+str(LiteralA))
                MyHelper.log('LiteralB='+str(LiteralB))
                MyHelper.log('notLiteralA='+str(notLiteralA))
                MyHelper.log('notLiteralB='+str(notLiteralB))
            
            if LiteralA == notLiteralB and LiteralB == notLiteralA:
                if debug2:
                    MyHelper.log('Found mutex in _negation')
                    MyHelper.log('literalA=' + str(literalA)) # e.g. Have(Cake)
                    MyHelper.log('literalB=' + str(literalB)) # e.g. Have(Cake)
                    MyHelper.log('----------')
                return True
            
        except Exception as ex:
            MyHelper.log_exception('Exception in _negation:', ex)
            return False

        return False


class PlanningGraph:
    def __init__(self, problem, state, serialize=True, ignore_mutexes=False):
        """
        Parameters
        ----------
        problem : PlanningProblem
            An instance of the PlanningProblem class

        state : tuple(bool)
            An ordered sequence of True/False values indicating the literal value
            of the corresponding fluent in problem.state_map

        serialize : bool
            Flag indicating whether to serialize non-persistence actions. Actions
            should NOT be serialized for regression search (e.g., GraphPlan), and
            _should_ be serialized if the planning graph is being used to estimate
            a heuristic
        """
        self._serialize = serialize
        self._is_leveled = False
        self._ignore_mutexes = ignore_mutexes
        self.goal = set(problem.goal)

        # make no-op actions that persist every literal to the next layer
        no_ops = [make_node(n, no_op=True) for n in chain(*(makeNoOp(s) for s in problem.state_map))]
        self._actionNodes = no_ops + [make_node(a) for a in problem.actions_list]
        
        # initialize the planning graph by finding the literals that are in the
        # first layer and finding the actions they they should be connected to
        literals = [s if f else ~s for f, s in zip(state, problem.state_map)]
        layer = LiteralLayer(literals, ActionLayer(), self._ignore_mutexes)
        layer.update_mutexes()
        self.literal_layers = [layer]
        self.action_layers = []

    # helper function used by two other functions: MaxLevel, LevelSum
    def h_levelcost(self, goal):

        debug1 = False
        debug2 = False

        try:            
            # scan level
            level = 0 
 
            for layer in self.literal_layers:
    
                if debug1:
                    MyHelper.log('function h_levelcost()')

                    # loop to see literals in layer
                    for literal in layer:
                        MyHelper.log('layer.literal=' + str(literal))
        
                    MyHelper.log('type(layer) = '+str(type(layer))) # <class 'my_planning_graph.LiteralLayer'>
                    MyHelper.log('goal = '+str(goal)) 
                    MyHelper.log('type(goal) = '+str(type(goal))) 
                
                    layer_set = set(list(layer))
                    MyHelper.log('type(layer_set) = '+str(type(layer_set))) 
                    MyHelper.log('layer_set = '+str(layer_set)) 
                    MyHelper.log('----------')

                # convert layer from object to set to use set build-in functions issubset() or issuperset()
                layer_set = set(list(layer))
                
                if set([goal]).issubset(layer_set):
                    if debug2:
                        MyHelper.log('Found level for goal in h_levelcost = '+str(level))
                        MyHelper.log('----------')

                    break
                        
                level += 1
        
            return level
        
        except Exception as ex:
            MyHelper.log_exception('Exception in h_levelcost:', ex)
            return None

        return None
        
        
    def h_levelsum(self):
        """ Calculate the level sum heuristic for the planning graph

        The level sum is the sum of the level costs of all the goal literals
        combined. The "level cost" to achieve any single goal literal is the
        level at which the literal first appears in the planning graph. Note
        that the level cost is **NOT** the minimum number of actions to
        achieve a single goal literal.
        
        For example, if Goal_1 first appears in level 0 of the graph (i.e.,
        it is satisfied at the root of the planning graph) and Goal_2 first
        appears in level 3, then the levelsum is 0 + 3 = 3.

        Hints
        -----
          - See the pseudocode folder for help on a simple implementation
          - You can implement this function more efficiently than the
            sample pseudocode if you expand the graph one level at a time
            and accumulate the level cost of each goal rather than filling
            the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)
        """
        # TODO: implement this function

        debug1 = False
        debug2 = False

        try:
            self.fill() # extend to maximum layers
            
            # total goal level add up
            level_sum = 0
            
            # next goal level
            level = 0 
            
            # loop goals, get level of each goal one by one
            for goal in self.goal:
                
                if debug1:
                    MyHelper.log('function h_levelsum()')
                    MyHelper.log('goal = '+str(goal))                   
                    MyHelper.log('----------')
                    
                level = self.h_levelcost(goal)
                level_sum += level
                
                if debug2:
                    MyHelper.log('level_sum in h_levelsum = '+str(level_sum))                   
                    MyHelper.log('----------')
        
            return level_sum
        
        except Exception as ex:
            MyHelper.log_exception('Exception in h_levelsum:', ex)
            return None

        return None

    # Max Level function version 1, superseded by improved version below
    def h_maxlevel_v1(self):
        """ Calculate the max level heuristic for the planning graph

        The max level is the largest level cost of any single goal fluent.
        The "level cost" to achieve any single goal literal is the level at
        which the literal first appears in the planning graph. Note that
        the level cost is **NOT** the minimum number of actions to achieve
        a single goal literal.

        For example, if Goal1 first appears in level 1 of the graph and
        Goal2 first appears in level 3, then the levelsum is max(1, 3) = 3.

        Hints
        -----
          - See the pseudocode folder for help on a simple implementation
          - You can implement this function more efficiently if you expand
            the graph one level at a time until the last goal is met rather
            than filling the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        Notes
        -----
        WARNING: you should expect long runtimes using this heuristic with A*
        """
        # TODO: implement maxlevel heuristic
        
        debug1 = False
        debug2 = False

        try:
            self.fill() # extend graph until level off, maximum layers
            
            # cost of achieving each goal
            costs = []            
            
            # loop goals, get level of each goal one by one
            for goal in self.goal:
                        
                if debug1:
                    MyHelper.log('function h_maxlevel()')
                    MyHelper.log('self.goal = '+str(self.goal))                   
                    MyHelper.log('----------')

                cost = self.h_levelcost(goal)
                
                if debug2:
                    MyHelper.log('Goal cost in h_maxlevel = '+str(cost))
                    MyHelper.log('----------')
                        
                costs.append(cost)
        
            return max(costs)
        
        except Exception as ex:
            MyHelper.log_exception('Exception in h_maxlevel:', ex)
            return None

        return None
    
    # Heuristics.md -  Improve Efficiency on function h_maxlevel(), decreased time by about 1s in unit test
    def h_maxlevel(self):
        """ Calculate the max level heuristic for the planning graph

        The max level is the largest level cost of any single goal fluent.
        The "level cost" to achieve any single goal literal is the level at
        which the literal first appears in the planning graph. Note that
        the level cost is **NOT** the minimum number of actions to achieve
        a single goal literal.

        For example, if Goal1 first appears in level 1 of the graph and
        Goal2 first appears in level 3, then the levelsum is max(1, 3) = 3.

        Hints
        -----
          - See the pseudocode folder for help on a simple implementation
          - You can implement this function more efficiently if you expand
            the graph one level at a time until the last goal is met rather
            than filling the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        Notes
        -----
        WARNING: you should expect long runtimes using this heuristic with A*
        """
        # TODO: implement maxlevel heuristic
        
        debug1 = False
        debug2 = False

        try:
            # extend graph by 1 level, for faster results
            # self.fill(1) # alternative way to extend graph level by 1
#            self._extend()
            
            # max level of achieving all goals
            level = 0
            
            if debug1:
                MyHelper.log('function h_maxlevel()')
            
            while not self._is_leveled:
            
                all_goals_met = True
                
                # get last literal layer
                last_literal_layer = self.literal_layers[-1]

                if debug1:
                    MyHelper.log('literal layers length = '+(str(len(self.literal_layers))))
                    MyHelper.log('last_literal_layer = '+str(last_literal_layer))
                
                # loop goals, get level of each goal one by one
                for goal in self.goal:
                            
                    if debug1:
                        MyHelper.log('self.goal = '+str(self.goal))                   
                        MyHelper.log('level = '+str(level))
                        MyHelper.log('----------')
    
                    if goal not in last_literal_layer:
                        all_goals_met = False
                        break
                    
                if all_goals_met:
                    if debug2:
                        MyHelper.log('All Goals met at level in h_maxlevel = '+str(level))
                        MyHelper.log('----------')
                    return level
                else:
                    if debug2:
                        MyHelper.log('graph extend by 1, at level '+str(level))
                    self._extend()
                    level += 1
            
            return None
        
        except Exception as ex:
            MyHelper.log_exception('Exception in h_maxlevel:', ex)
            return None

        return None
        
    def h_setlevel(self):
        """ Calculate the set level heuristic for the planning graph

        The set level of a planning graph is the first level where all goals
        appear such that no pair of goal literals are mutex in the last
        layer of the planning graph.

        Hints
        -----
          - See the pseudocode folder for help on a simple implementation
          - You can implement this function more efficiently if you expand
            the graph one level at a time until you find the set level rather
            than filling the whole graph at the start.

        See Also
        --------
        Russell-Norvig 10.3.1 (3rd Edition)

        Notes
        -----
        WARNING: you should expect long runtimes using this heuristic on complex problems
        """
        # TODO: implement setlevel heuristic
        
        # find all goals exist together in one single layer, and all goals are not mutex
        
        debug1 = False
        debug2 = False

        try:
            if debug1:
                MyHelper.log('function h_setlevel()')

            self.fill() # extend graph until level off, maximum layers
            
            level = 0
            
            # scan layer one by one
            for layer in self.literal_layers:
    
                # convert layer from object to set to use set build-in functions issubset() or issuperset()
                layer_set = set(list(layer))
                
                # 1. find all goals exist together in one single layer
                
                # method 1 - one liner, check all goals is subset of the layer literals
                all_goals_met = self.goal.issubset(layer_set)

                # method 2 - loop goal one by one (not used)
#                all_goals_met = True
#
#                # loop goals one by one
#                for goal in self.goal:                            
#                    if debug1:
#                        MyHelper.log('goal = '+str(goal))                   
#                        MyHelper.log('----------')
#               
#                    if not set([goal]).issubset(layer_set):
#                        if debug2:
#                            MyHelper.log('Goal is not found in layer in h_setlevel = '+str(goal))
#    
#                        all_goals_met = False
#                        
#                        # break goal loop, but continue scan on next layer
#                        break
                        
                # if not found all the goals in one layer, continue to scan the next layer
                if all_goals_met == False:
                    level += 1
                    continue
                else:
                    if debug2:
                        MyHelper.log('all_goals_met = '+str(True))
                
                # 2. if all goals met in one layer, then all goals need to be not mutex
                goals_are_mutex = False
                
                for goal1 in self.goal:
                    for goal2 in self.goal:
                        
                        # not check same goal
                        if goal1 is goal2:
                            continue
                        
                        if layer.is_mutex(goal1, goal2) or layer.is_mutex(goal2, goal1):
                            goals_are_mutex = True
                            break;
                    if goals_are_mutex:
                        break
                
                # 3. if no mutex found, return layer level index
                if not goals_are_mutex:
                    if debug2:
                        MyHelper.log('goals_are_mutex = '+str(False))
                        MyHelper.log('found level = '+str(level))
                        MyHelper.log('----------')                       
                    return level

                if debug2:
                    MyHelper.log('----------')
 
                level += 1
            
            return None
        
        except Exception as ex:
            MyHelper.log_exception('Exception in h_setlevel:', ex)
            return None

        return None


    ##############################################################################
    #                     DO NOT MODIFY CODE BELOW THIS LINE                     #
    ##############################################################################

    def fill(self, maxlevels=-1):
        """ Extend the planning graph until it is leveled, or until a specified number of
        levels have been added

        Parameters
        ----------
        maxlevels : int
            The maximum number of levels to extend before breaking the loop. (Starting with
            a negative value will never interrupt the loop.)

        Notes
        -----
        YOU SHOULD NOT THIS FUNCTION TO COMPLETE THE PROJECT, BUT IT MAY BE USEFUL FOR TESTING
        """
        while not self._is_leveled:
            if maxlevels == 0: break
            self._extend()
            maxlevels -= 1
        return self

    def _extend(self):
        """ Extend the planning graph by adding both a new action layer and a new literal layer

        The new action layer contains all actions that could be taken given the positive AND
        negative literals in the leaf nodes of the parent literal level.

        The new literal layer contains all literals that could result from taking each possible
        action in the NEW action layer. 
        """
        if self._is_leveled: return

        parent_literals = self.literal_layers[-1]
        parent_actions = parent_literals.parent_layer
        action_layer = ActionLayer(parent_actions, parent_literals, self._serialize, self._ignore_mutexes)
        literal_layer = LiteralLayer(parent_literals, action_layer, self._ignore_mutexes)

        for action in self._actionNodes:
            # actions in the parent layer are skipped because are added monotonically to planning graphs,
            # which is performed automatically in the ActionLayer and LiteralLayer constructors
            if action not in parent_actions and action.preconditions <= parent_literals:
                action_layer.add(action)
                literal_layer |= action.effects

                # add two-way edges in the graph connecting the parent layer with the new action
                parent_literals.add_outbound_edges(action, action.preconditions)
                action_layer.add_inbound_edges(action, action.preconditions)

                # # add two-way edges in the graph connecting the new literaly layer with the new action
                action_layer.add_outbound_edges(action, action.effects)
                literal_layer.add_inbound_edges(action, action.effects)

        action_layer.update_mutexes()
        literal_layer.update_mutexes()
        self.action_layers.append(action_layer)
        self.literal_layers.append(literal_layer)
        self._is_leveled = literal_layer == action_layer.parent_layer

