#!/usr/bin/env python
import math
import features


def get_entropy_hash(feature_list,data):
    to_return = {}
    for f in feature_list:
        x = get_entropy(f, data)
        to_return[x] = f

    return to_return

def create_majority_label(data):
        majority_label = None
        labels = {}
        for i in data:
            if i not in labels:
                labels[i] = []

            labels[i].append(data[i])

        for k in labels.keys():
            if majority_label is None:
                majority_label = k
            else:
                if len(labels[majority_label]) < len(labels[k]):
                    majority_label = k

        # Now we have our majority label, we will define a new function
        # in the features module so that we can use this later
        def _majority_label(label=labels[majority_label]):
            return label

        features.majority_label = _majority_label

def reduce_entropy(node, feature_list, data):
    """
       Params:
           node is a new node with a label
           feature_list is a set of features to consider
           data is a set of examples to classify

    """
    # First, classify all examples using this feature
    from pprint import pprint
    pprint("I am node %s" % node.label)
    pprint("My data size is %s" % len(data))

    if len(data) == 0:
        node.label = 'majority_label'
        return

    return_vals = {}
    for d in data.keys():
        l = getattr(features, node.label)(d)
        if l not in return_vals:
            return_vals[l] = {}

        return_vals[l][d] = data[d]

    # if all examples have the same label, we return
    if len(return_vals) == 1:
        pprint("All of my data classifies the same way")
        return

    # Now add a child for each classification
    # XXX: Can't assume that all possible classications will be returned, fix this!

    if node.label == 'has_middle_name':
        import pdb; pdb.set_trace()
    if len(feature_list) > 0:
        feature_list = get_entropy_hash(feature_list.values(), data)
    for i in return_vals:
        try:
            low = sorted(feature_list.keys())[0]
            new_node = Node(label=feature_list[low],parent=node, data=return_vals[i])
            del(feature_list[low])
            node.children.append(new_node)
        except IndexError:
            return

    for child in node.children:
        pprint("Child %s-> parent %s" % (child.label, child.parent.label))

        reduce_entropy(child, feature_list, child.data)



def get_tree(data, feature_list):
    '''
       Take data, get a decision tree based on the id3 algorithm.
    '''
    # Set up majority label function:
    create_majority_label(data)

    # First get entropy for all features:
    entropy_feature = get_entropy_hash(feature_list,data)

    # Now, choose the lowest entropy, split on that node
    low = sorted(entropy_feature.keys())[0]

    root = Node(label=entropy_feature[low], data=data, is_root=True)
    del(entropy_feature[low])
    reduce_entropy(root, entropy_feature, data)

    return root

def get_entropy(feature, data):
    yes = 0
    no = 0
    for k in data.keys():
        # If it classifies as true
        if getattr(features, feature)(k):
            if data[k]:
                yes = yes + 1
            else:
                no = no + 1
        else:
        #If it classifies as false
            pass



    avg_yes = float(yes) / (len(data))
    avg_no = float(no) / (len(data))
    #import pdb; pdb.set_trace()

    if avg_yes == 0:
        return abs(avg_no * math.log(avg_no,2) )

    if avg_no == 0:
        return abs(avg_yes * math.log(avg_yes,2) )

    return abs( (avg_yes * math.log(avg_yes,2) ) - (avg_no * math.log(avg_no,2)) )


class id3_tree(object):
    '''
       id3_tree should be able to output several things:
           * Show a trace of how decision tree was built
           ** Show entropy step
           ** Show information gain step
           * Show a representation of the tree
           * A classifier that can take data and give a classification

       functional methods:
           * Modify tree based on hyper-parameters
           ** Depth

       in addition some utility methods might be nice:
           * take representation of decision tree, build object

    '''
    def __init__(self, root=None):
        self.root = root

        if root != None:
            root.is_root = True

    def classify(self, node=None):
        """Use the current tree to classify all the things"""
        pass

    def traverse(self):
        r = self.root

        def _in_order_traverse(node=None):
            to_return = []
            if node == None:
                return to_return

            from pprint import pprint; pprint("Now recursing on: %s" % node)
            pprint("This many children: %s" % len(node.children))
            if len(node.children) > 0:
                pprint("How am I passing this conditional")
            if len(node.children) > 0:
                for child in node.children:
                    return to_return.extend(_in_order_traverse(child))

            return to_return

        return _in_order_traverse(r)




class Node():
    def __init__(self, parent=None, label=None,
            data=None, childs=None,  is_root=False):
        self.parent = parent
        self.children = childs
        self.label = label
        self.data = data
        self.is_root = is_root

        if self.children is None:
            self.children = []

        if label == None:
            raise RequiredFieldException

        if parent == None:
            if is_root == False:
                raise RequiredFieldException

    def __str__(self):
        return "Me: %s\nChildren: %s" % (self.label,self.children)

    def __unicode__(self):
        self.__str__()

    def get_root(self):
        if self.is_root:
            return self

        self.parent.get_root()

class RequiredFieldException(Exception):
    pass
