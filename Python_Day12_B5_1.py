#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing modules:

# let us consider a scenario that team of five members planned to do as below in first day:
    
#    team member name  --->    first day work ---->  second day work
#    -----------------       -----------------       ---------------
#    bunty             --->     a             --->     c
#    jyothi            --->     b             --->     a
#    danish            --->     c             --->     e
#    bhargavi          --->     d             --->     b
#    karuni            --->     e             --->     d


# In[ ]:


# above representation shows that each team member done with their work during first day.
# In the second day each team member asked to continue with the work that was done by other team member.
# so in this case in each team member will import the firstday code from code storage and do enhancements on top of that 
#    instead of doing from initial.
    
# ***** importing existing code into system is called as IMPORTING MODULE  *****


# In[ ]:


# let us consider that 5 friends planned to order a pizza 
# so here considerations are  size & topping as per the person's choice
#  *** can pass multiple arguments here ***


# In[1]:


# lets define function

def make_pizza(size,*toppings):    # * --> show that passing multiple arguments
    """Summarize the pizza that we are going to order"""
    print(f"\nMaking a {size} - inch pizza")
    for topping in toppings:
        print(f"--{topping}")


# In[ ]:




