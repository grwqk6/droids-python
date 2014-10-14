class cache:
  enemy_hangars =[]
  enemy_droids=[]
  my_droids=[]
  walls=[]

  ai=None

  de__init--(self,ai):
    self.ai = ai
    
    self.walls = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]]
    self.my_droids =[[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]]
    self.enemy_droids = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]]
    self.enemy_hangars = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]]

    def update_droids(self):
     for droid in self.ai.droids:
