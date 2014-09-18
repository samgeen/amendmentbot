'''
List of templates for amendmentbot
Sam Geen & Mike Cook, August 2014
'''

templates = ["Protects the right to VERB OBJECTS in PLACE",
              "Protects the right to ACTION according to RULESOURCE",
              "Prohibits ACTION and sets out requirements for SAME "+\
                           "based on RULESOURCE "+\
                           "according to a federal judge",
              "Sets out rules for ACTION by PEOPLE",
              "Provides the right to ACTION in certain EVENTS",
              "Limits the powers of the federal government to ACTION",
              "The NUMBERTH amendment is hereby repealed",
              "The VERBTGTED of OBJECTS is hereby prohibited",
              "In the case of the VERBTGTED of the President, the Vice President shall "+\
              "VERB OBJECTS",
              "Prohibits VERBTGTED of OBJECTS in PLACE during EVENTS",
              "Prohibits ACTION and ACTION and sets out requirement s for SAME based on RULESOURCE",
             "Revises presidential VERBTGTED procedures",
             "Abolishes ACTION and ACTION except as punishment for a crime",
             "Defines VERBTGTED, contains the CAP OBJECTS Clause, the OBJECTS NOCAP Clause, and deals with post-VERBTGTED issues",
             "Protects OBJECTS not enumerated in the constitution",
             "Prohibits the denial of the right to ACTION based on RULESOURCE, RULESOURCE or RULESOURCE",
             "Prohibits the denial of the right to ACTION based on RULESOURCE",
             "Changes the date on which EVENTS (January NUMBERTH) end and begin",
             "Repeals the NUMBERTH amendment and prohibits the VERBTGTED or VERBTGTED into the United States of OBJECTS",
             "Grants PLACE PEOPLE (the number of SAME being equal to the least populous state) in the Electoral College",
             "Prohibits the VERBTGTED of PEOPLE due to the VERBTGTED of OBJECTS",
             "Addresses the VERBTGTED of the President and establishes procedues for the Vice President ACTION",
             "Delays laws affecting Congressional salary from taking effect until after the next VERBTGTED of PEOPLE",
             "Deals with ACTION by PEOPLE according to RULESOURCE as determined by a federal judge",
             "Limits the powers of the President to ACTION in EVENTS",
             "Prohibits the VERBTGTED of OBJECTS by PEOPLE according to RULESOURCE",
             "Limits the VERBTGTED of the Vice President; the Vice President may not VERB OBJECTS except in EVENTS",
             "Prohibits the VERBTGTED of OBJECTS by the President except in EVENTS",
             "Addresses VERBTGTED of the President and Vice President and establishes procedures for ACTION",
             "Prohibits the denial of the right of PEOPLE to VERB beyond their NUMBERTH birthday on account of age",
             "Prohibits ACTION in PLACE except in EVENTS",
             "Prohibits the ACTION or ACTION within the United States",
             "Establishes the direct VERBTGTED of PEOPLE by popular vote",
             "Permits Congress to VERB OBJECTS without VERBTGTED among the states or basing it on RULESOURCE",
             "Revises presidential VERBTGTED procedures",
             "Makes PLACE immune from suits from out-of-state PEOPLE and PEOPLE not living within the state borders",
             "Prohibits excessive OBJECTS and excessive OBJECTS, as well as cruel and unsual VERBTGTED",
             "Protects OBJECTS not enumerated in the Constitution",
             "Protects the right to VERB and VERB OBJECTS",
             "Protects the right to VERB OBJECTS",
             "Prohibits the VERBTGTED of PEOPLE in PLACE during peacetime",
             "Reinforces the principle of RULESOURCE in EVENTS",
             "Prohibits PEOPLE from ACTION according to a federal judge",
             "Makes PEOPLE immune from suits from PEOPLE not living within PLACE",
             "Repeals the NUMBERTH amendment and lays out rules for the VERBTGTED of PEOPLE by Congress",
             "Abolishes ACTION, and ACTION, except as punishment for a crime",
             "Prohibits Congress from ACTION except in EVENTS",
             "Abolishes the VERBTGTED of the President except in EVENTS",
             "Sets out rules for the VERBTGTED of OBJECTS by PEOPLE",
             "Revises vice-presidential VERBTGTED procedures"
              ]

if __name__=="__main__":
    import abot
    for template in templates:
        print abot.runfortemplate(template)
    print len(templates), "TEMPLATES SO FAR"
