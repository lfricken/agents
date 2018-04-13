from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.agents import base_agent
from pysc2.lib import actions


class SaveSimulationResults(base_agent.BaseAgent):
    start_units_1 = dict([(0, 0)])
    start_units_2 = dict([(0, 0)])
    end_units_1 = dict([(0, 0)])
    end_units_2 = dict([(0, 0)])
    num_step = 0

    def clean(self):
        self.start_units_1 = dict([(0, 0)])
        self.start_units_2 = dict([(0, 0)])
        self.end_units_1 = dict([(0, 0)])
        self.end_units_2 = dict([(0, 0)])
        self.num_step = 0

    def increment(self, units, unit_type):
        if unit_type in units:
            units[unit_type] += 1
        else:
            units[unit_type] = 1

    def add(self, player, unit_type, isStart):
        if isStart:
            if player == 1:
                self.increment(self.start_units_1, unit_type)
            else:
                self.increment(self.start_units_2, unit_type)
        else:
            if player == 1:
                self.increment(self.end_units_1, unit_type)
            else:
                self.increment(self.end_units_2, unit_type)

    def get_units(self, obs, isStart):
        units_arr = obs[3]["units"]
        for unit in units_arr:
            self.add(unit.owner, unit.unit_type, isStart)

    def step(self, obs):
        if obs.first():
            self.clean()
            self.get_units(obs, True)

        if obs.last():
            self.get_units(obs, False)

            with open('units.txt', 'a') as data:
                data.write("\n")
                data.write("\n")
                data.write(str(self.start_units_1))
                data.write(str(self.start_units_2))

                data.write("\n")
                data.write(str(self.end_units_1))
                data.write(str(self.end_units_2))

        return actions.FunctionCall(0, [])
