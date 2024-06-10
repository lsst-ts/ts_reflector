# This file is part of ts_reflector.
#
# Developed for the Vera C. Rubin Observatory Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
__all__ = ["command_reflector"]

import asyncio

from lsst.ts import salobj


class ReflectorCommander(salobj.CscCommander):
    """Reflector commander.

    Parameters
    ----------
    enable : bool
        Enable the CSC when first connecting to it?
    """

    def __init__(self, enable: bool) -> None:
        super().__init__(
            name="Reflector",
            index=0,
            enable=enable,
        )


def command_reflector() -> None:
    """Run the Reflector commander."""
    asyncio.run(ReflectorCommander.amain(index=None))
