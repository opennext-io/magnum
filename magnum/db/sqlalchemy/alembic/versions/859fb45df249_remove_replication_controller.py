#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""remove replication controller

Revision ID: 859fb45df249
Revises: 1f196a3dabae
Create Date: 2016-08-09 13:46:24.052528

"""

# revision identifiers, used by Alembic.
revision = '859fb45df249'
down_revision = '1f196a3dabae'

from alembic import op


def upgrade():
    op.drop_table('replicationcontroller')
