from random import randint

class autopsy(object):
    """description of class"""

    def set_build(self, creature_type):
        build = randint(1,5)
        #extend to other creature descriptions
        if build == 1: self.build_desc = SKELETAL
        elif build == 2: self.build_desc = LEAN
        elif build == 3: self.build_desc = FIT
        elif build == 4: self.build_desc = PUDGY
        elif build == 5: self.build_desc = OBESE

    def set_face_features(self, creature_type):
        build = randint(1,18)
        if build == 1: self.face_desc = GAUNT
        elif build == 2: self.face_desc = NO_LEFT_EYE
        elif build == 3: self.face_desc = NO_RIGHT_EYE
        elif build == 4: self.face_desc = NO_NOSE
        elif build == 5: self.face_desc = NO_TEETH
        elif build == 6: self.face_desc = NO_LEFT_EAR
        elif build == 7: self.face_desc = NO_RIGHT_EAR
        elif build == 8: self.face_desc = BROKEN_NOSE
        elif build == 9: self.face_desc = BROKEN_TEETH
        elif build == 10: self.face_desc = BROKEN_LEFT_SOCKET
        elif build == 11: self.face_desc = BROKEN_RIGHT_SOCKET
        elif build == 12: self.face_desc = LUMP_LEFT_CHEEK
        elif build == 13: self.face_desc = LUMP_RIGHT_CHEEK
        elif build == 14: self.face_desc = LUMP_LEFT_EYEBROW
        elif build == 15: self.face_desc = LUMP_RIGHT_EYEBROW
        elif build == 16: self.face_desc = LUMP_UPPER_LIP
        elif build == 17: self.face_desc = LUMP_LOWER_LIP
        else: self.face_desc = BLUE_VEINS

    def set_torso_features(self, creature_type):
        build = randint(1,5)
        if build == 1: self.torso_desc = GAUNT
        elif build == 2: self.torso_desc = SCARRED
        elif build == 3: self.torso_desc = BLOATED
        elif build == 4: self.torso_desc = LEFT_CHEST_SCARRED
        elif build == 5: self.torso_desc = RIGHT_CHEST_SCARRED
        elif build == 6: self.torso_desc = STOMACH_SCARRED
        elif build == 7: self.torso_desc = LEFT_CHEST_FOREIGN
        elif build == 8: self.torso_desc = RIGHT_CHEST_FOREIGN
        elif build == 9: self.torso_desc = STOMACH_FOREIGN
        elif build == 10: self.torso_desc = BROKEN_RIBS
        elif build == 11: self.torso_desc = TWISTED_SPINE
        else: self.torso_desc = BLUE_VEINS

    def set_arms_features(self, creature_type):
        build = randint(1,5)
        if build == 1: self.arms_desc = GAUNT
        elif build == 2: self.arms_desc = SCARRED
        elif build == 2: self.arms_desc = LEFT_SCARRED
        elif build == 2: self.arms_desc = RIGHT_SCARRED
        elif build == 2: self.arms_desc = LEFT_MISHAPEN
        elif build == 2: self.arms_desc = RIGHT_MISHAPEN
        elif build == 2: self.arms_desc = LEFT_ROUGH_SCALES
        elif build == 2: self.arms_desc = RIGHT_ROUGH_SCALES
        elif build == 2: self.arms_desc = LEFT_INFECTION
        elif build == 2: self.arms_desc = RIGHT_INFECTION
        else: self.arms_desc = BLUE_VEINS

    def set_legs_features(self, creature_type):
        build = randint(1,5)
        if build == 1: self.legs_desc = GAUNT
        elif build == 2: self.legs_desc = SCARRED
        elif build == 2: self.legs_desc = LEFT_SCARRED
        elif build == 2: self.legs_desc = RIGHT_SCARRED
        elif build == 2: self.legs_desc = LEFT_MISHAPEN
        elif build == 2: self.legs_desc = RIGHT_MISHAPEN
        elif build == 2: self.legs_desc = LEFT_ROUGH_SCALES
        elif build == 2: self.legs_desc = RIGHT_ROUGH_SCALES
        elif build == 2: self.legs_desc = LEFT_INFECTION
        elif build == 2: self.legs_desc = RIGHT_INFECTION
        else: self.legs_desc = BLUE_VEINS

    def get_visual(self, creature_type):
        Text = []
        Text.append("EXTERNAL EXAMINATION:")
        if creature_type == "human":
            Text.append("The body is that of a middle aged {self.sex} human of average height and build.")
            ## https://www.utmb.edu/meded/year4/autopsy_4th_year/autopsyreportsample.pdf
        if creature_type == "human":
            if self.build_desc == SKELETAL:
                Text.append("The human seems to have been at the edge of starvation before death. It appears")
                Text.append("the suffering of this poor creature was remedied by our actions most fortunatly.")
            if self.build_desc == LEAN:
                Text.append("The human seems to have been having a poor time at thier chosen profession. Some")
                Text.append("say that is the slings and arrows of life - we were the last straw in a long line")
                Text.append("of bad choices.")
            if self.build_desc == FIT:
                Text.append("The human seems to have wonderful musculature, possibly owing to a life of labor,")
                Text.append("or a natural adaptation to the life of a wayfarer. Despite the state of death, they")
                Text.append("are still pleasnt to look at. I must not let that detract from my findings.")
            if self.build_desc == PUDGY:
                Text.append("The human seems to have had a relaxed and privledged life up until our encounter.")
                Text.append("Large, healthy deposits of fat suggest that they were well nourished and that the")
                Text.append("position they were in was one of calm.")

        if creature_type == "human":
            if self.face_desc == GAUNT:
                Text.append("The face is shallow and hollow, with not much fat or muscle across it. The skin")
                Text.append("is streched tightly accross it, sumptomizing a problem with nutrition or health.")
            elif self.face_desk == NO_LEFT_EYE:
                Text.append("The face, while strong and healthy, has recieved a battle wound to the left side,")
                Text.append("removing the eye from it's socket and leaving a deep tissue scar. Otherwise, face")
                Text.append("seems in tact.")
            elif self.face_desk == NO_RIGHT_EYE:
                Text.append("The face, while strong and healthy, has recieved a battle wound to the right side,")
                Text.append("sealing the remains of the eye in it's socket and leaving a deep tissue scar. Otherwise, face")
                Text.append("seems in tact.")
            elif self.face_desk == NO_NOSE:
                Text.append("The face as at one point recieved a brutal cut to where the nose once was, exposing the")
                Text.append("deep nasal cavity and giving the face the look of a corpse. Other then the ghastly")
                Text.append("impression, seems otherwise in tact and healthy.")
            elif self.face_desk == NO_TEETH:
                Text.append("The cheeks are hollow and impacted - on closer inspection, only the rotten remains")
                Text.append("of roots can be found within. How this human has survived to this point is beyond you.")
            elif self.face_desk == NO_LEFT_EAR:
                Text.append("The left side of the face of this human has a large scar running across it, and")
                Text.append("the ear has been completely removed as well as a portion of the scalp. The wound")
                Text.append("has long since healed, but it is doubtful the bearer could use it.")
            elif self.face_desk == NO_RIGHT_EAR:
                Text.append("The right side of the face of this human has a large burn stretching across it.")
                Text.append("The ear has been completely burned off as well as a portion of the scalp. The wound")
                Text.append("has long since healed, but it is doubtful the bearer could use the ear.")
            elif self.face_desk == BROKEN_NOSE:
                Text.append("The nose of this individual has been completely smashed down, probably due to an")
                Text.append("old fight injury. The noise this individual must have made breathing while alive")
                Text.append("must have been incredible.")
            elif self.face_desk == BROKEN_TEETH:
                Text.append("Your eyes are drawn to the gash of a mouth this individual has - parting the scarred")
                Text.append("lips reveal rows of broken and chipped teeth and a shredded, still bleeding tongue.")
                Text.append("What caused this?")
            elif self.face_desk == BROKEN_LEFT_SOCKET:
                Text.append("The face on this human could be considered rugged, and it not been for a large injury")
                Text.append("to the left eye socket, breaking the bone and crushing it down. It looks like it happened")
                Text.append("long enough in the past for it to have healed completely.")
            elif self.face_desk == BROKEN_RIGHT_SOCKET:
                Text.append("The face on this human could be considered rugged, and it not been for a large injury")
                Text.append("to the right eye socket. The eye itself is a mangled mass of blood, meat and puss, suggesting")
                Text.append("the injury is fairly recent.")
            elif self.face_desk == LUMP_LEFT_CHEEK:
                Text.append("The most startling feature is a large, fat lump protruding from the left cheeck. Slicing")
                Text.append("into the lump leads to a large mass of scar tissue, but no indication where it comes from.")
            elif self.face_desk == LUMP_RIGHT_CHEEK:
                Text.append("The most startling feature is a large, fat lump protruding from the left cheeck. Slicing")
                Text.append("into the lump leads to a large mass of scar tissue speckled with fat, but no indication")
                Text.append("where it comes from.")
            elif self.face_desk == LUMP_LEFT_EYEBROW:
                Text.append("The most startling feature is a large, fat lump protruding from the left eyebrow. Slicing")
                Text.append("through the scars, several lumps of stone are weaved through the fat.")
            elif self.face_desk == LUMP_RIGHT_EYEBROW:
                Text.append("The most startling feature is a large, fat lump protruding from the right eyebrow. Slicing")
                Text.append("through the scars, several lumps of calcified bone are weaved through the fat.")
            elif self.face_desk == LUMP_UPPER_LIP:
                Text.append("The most startling feature is a large, fat lump protruding from the upper lip. Slicing")
                Text.append("through the scars, a foul smelling green liquid spills out.")
            elif self.face_desk == LUMP_LOWER_LIP:
                Text.append("The most startling feature is a large, fat lump protruding from the lower lip. Slicing")
                Text.append("through the scars, a foul smelling green liquid spills out.")

        if creature_type == "human":
            if self.torso_desc == GAUNT:
                if self.sex == MALE :
                    Text.append("The chest is thin and the skin is streched tightly across the bone. The stomach")
                    Text.append("skin, in contrast, is pulled into the rib cage but also slightly loose, suggesting")
                    Text.append("it was once covering a much more formidible form.")
                if self.sex == FEMALE :
                    Text.append("The chest is thin and the skin is streched tightly across the bone. The stomach")
                    Text.append("skin, in contrast, is pulled into the rib cage but also slightly loose, suggesting")
                    Text.append("it was once covering a much more formidible form. The breasts are all but invisible.")

        Text.append(" ------- ")
        Text.append("INTERNAL EXAMINATION(BODY CAVITIES):")

        if creature_type == "human":
            Text.append("The right and left cavity contains semi-clear fluid of unknown origin. This fluid")
            Text.append("has an abscense of blood or blud essence, so will be ignored. Pericardial sack is")
            Text.append("yellow and glistening, without any adhesions and contains a yellow, straw colored")
            Text.append("fluid that reacts to blud. Decanting for further use.")
            
        Text.append(" ------- ")
        Text.append("Heart:")

        if creature_type == "human":
            Text.append("The heart is large and of normal shape, with a weight of about 4 stone. Deep")
            Text.append("examination of the heart has lead to the reveloution that it is normal for the age")
            Text.append("and sex of the corpse. Approximatly a cup of blud-diffuse crystaline fat surrounds")
            Text.append("the sac, and has been collected with the organ for further use.")

        Text.append(" ------- ")
        Text.append("Lungs:")

        if creature_type == "human":
            Text.append("Left and right lungs are approximatly the same size and shape, although the left")
            Text.append("appears to be a stone or so heavier than the right. Yellow fluid has been retrieved")
            Text.append("from both sides of the organ, but this seems to have no reaction to blud and has been")
            Text.append("contaminated with blood from expiry, so will be discarded. Approximatly 1 1/2 cups of")
            Text.append("additional blud-diffuse crystaline fat has been retrieved as well with the organs.")

        Text.append(" ------- ")
        Text.append("Intestinal tract:")

        if creature_type == "human":
            Text.append("Stomach and essophogas seem remarkably normal, asside from damage taken during final")
            Text.append("fight. No ulcers or nodules can be seen lining the surface, indicating that the")
            Text.append("individual was healthy in most respects. Stomach contains 5 cups of unidentified")
            Text.append("matter that has been discarded. The Pancreas appears fine, as well as the colon,")
            Text.append("liver, gallbladder and the bile ducts that connect. Small and large intestines are")
            Text.append("unremarkable.")

        Text.append(" ------- ")
        Text.append("Lower organs:")

        if creature_type == "human":
            Text.append("Kidenys and glandular structure appears normal.")

        Text.append(" ------- ")
        Text.append("Brain:")

        if creature_type == "human":
            Text.append("The brain inside the skull cavity seems largly in tact, and devoid of scarring or")
            Text.append("adhesions which would belay a violent or poorly life. The cerebral hemispheres are")
            Text.append("clearly defined. Aproximatly two cups of cerebrospinal fluid has been decanted and")
            Text.append("is awaiting use.")

        Text.append(" ------- ")
        Text.append("Convlusion:")

        Text.append("Remaining meat has been rendered down and seperated from the bone for other projects.")
        Text.append("About 24 stone of bone, added to storage for other projects.")