##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Database Tools",
    "version": "9.0.1.4.0",
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'category': "Extra Tools",
    'depends': [
        'server_mode',
        'base_setup',
    ],
    'external_dependencies': {
        'python': ['fabric']
    },
    'data': [
        'wizard/db_database_backup_now_wizard_view.xml',
        'views/database_backup_view.xml',
        'views/database_view.xml',
        'views/database_preserve_view.xml',
        'security/ir.model.access.csv',
        'data/backups_preserve_rules_data.xml',
        'data/backup_data.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
