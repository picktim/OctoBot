#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import abc

import octobot.automation.bases.automation_step as automation_step


class AbstractTriggerEvent(automation_step.AutomationStep, abc.ABC):
    def __init__(self):
        super(AbstractTriggerEvent, self).__init__()
        self.should_stop = False

    async def stop(self):
        self.should_stop = True

    async def _get_next_event(self):
        raise NotImplementedError

    async def next_event(self):
        """
        Async generator, use as follows:
            async for event in self.next_event():
                # triggered when an event occurs
        """
        while not self.should_stop:
            yield await self._get_next_event()



