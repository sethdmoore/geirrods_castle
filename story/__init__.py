class Campaign(object):
    def __init__(self, scenario):
        self.scenario = scenario

    def Chapter(self, key):
        # update the state of the object
        self.text  = "\n".join(self.scenario[key]["scenario"])

        self.choices = self.scenario[key]["valid_choices"]
        self.lethal_choices = self.scenario[key]["lethal_choices"]

        print(self.text)

    def valid_choices(self, key):
        return self.choices
        # if key in self.text:
        #     print("\n".join((output)))
        # else:
        #     print("ERROR: chapter not in story")
