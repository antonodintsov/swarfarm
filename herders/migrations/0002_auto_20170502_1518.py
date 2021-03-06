# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 22:18
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0001_squashed_0003_remove_monstertag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='affected_stat',
            field=models.IntegerField(blank=True, choices=[(0, 'HP'), (1, 'ATK'), (2, 'DEF'), (3, 'SPD'), (4, 'CRI Rate'), (5, 'CRI Dmg'), (6, 'Resistance'), (7, 'Accuracy'), (8, 'Max. Energy'), (9, 'Mana Stone Storage'), (10, 'Mana Stone Production Rate'), (11, 'Energy Production Rate'), (12, 'Arcane Tower ATK'), (13, 'Arcane Tower SPD')], null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='area',
            field=models.IntegerField(blank=True, choices=[(0, 'Everywhere'), (1, 'Guild Battle')], null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='element',
            field=models.CharField(blank=True, choices=[('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='gameevent',
            name='day_of_week',
            field=models.IntegerField(blank=True, choices=[(6, 'Sunday'), (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday')], null=True),
        ),
        migrations.AlterField(
            model_name='gameevent',
            name='element_affinity',
            field=models.CharField(choices=[('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gameevent',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='America/Los_Angeles'),
        ),
        migrations.AlterField(
            model_name='gameevent',
            name='type',
            field=models.IntegerField(choices=[(1, 'Elemental Dungeon'), (2, 'Special Event')]),
        ),
        migrations.AlterField(
            model_name='monster',
            name='archetype',
            field=models.CharField(choices=[('attack', 'Attack'), ('hp', 'HP'), ('support', 'Support'), ('defense', 'Defense'), ('material', 'Material')], default='attack', max_length=10),
        ),
        migrations.AlterField(
            model_name='monster',
            name='base_stars',
            field=models.IntegerField(choices=[(1, '1<span class="glyphicon glyphicon-star"></span>'), (2, '2<span class="glyphicon glyphicon-star"></span>'), (3, '3<span class="glyphicon glyphicon-star"></span>'), (4, '4<span class="glyphicon glyphicon-star"></span>'), (5, '5<span class="glyphicon glyphicon-star"></span>'), (6, '6<span class="glyphicon glyphicon-star"></span>')]),
        ),
        migrations.AlterField(
            model_name='monster',
            name='element',
            field=models.CharField(choices=[('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], default='fire', max_length=6),
        ),
        migrations.AlterField(
            model_name='monsterinstance',
            name='notes',
            field=models.TextField(blank=True, help_text='<a href="https://daringfireball.net/projects/markdown/syntax" target="_blank">Markdown syntax</a> enabled', null=True),
        ),
        migrations.AlterField(
            model_name='monsterinstance',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], null=True),
        ),
        migrations.AlterField(
            model_name='monsterleaderskill',
            name='area',
            field=models.IntegerField(choices=[(1, 'General'), (2, 'Dungeon'), (3, 'Element'), (4, 'Arena'), (5, 'Guild')], default=1),
        ),
        migrations.AlterField(
            model_name='monsterleaderskill',
            name='attribute',
            field=models.IntegerField(choices=[(1, 'HP'), (2, 'Attack Power'), (3, 'Defense'), (4, 'Attack Speed'), (5, 'Critical Rate'), (6, 'Resistance'), (7, 'Accuracy'), (8, 'Critical DMG')]),
        ),
        migrations.AlterField(
            model_name='monsterleaderskill',
            name='element',
            field=models.CharField(blank=True, choices=[('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='all',
            field=models.BooleanField(default=False, help_text='This effect affects all items on the target'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='aoe',
            field=models.BooleanField(default=False, help_text='Effect applies to entire friendly or enemy group'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='chance',
            field=models.IntegerField(blank=True, help_text='Chance of effect occuring per hit', null=True),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='damage',
            field=models.BooleanField(default=False, help_text='Amount of this effect is based on damage dealt'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='note',
            field=models.TextField(blank=True, help_text="Explain anything else that doesn't fit in other fields", null=True),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='quantity',
            field=models.IntegerField(blank=True, help_text='Number of items this effect affects on the target', null=True),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='random',
            field=models.BooleanField(default=False, help_text='Skill effect applies randomly to the target'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='self_effect',
            field=models.BooleanField(default=False, help_text='Effect applies to the monster using the skill'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='self_hp',
            field=models.BooleanField(default=False, help_text="Amount of this effect is based on casting monster's HP"),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='single_target',
            field=models.BooleanField(default=False, help_text='Effect applies to a single monster'),
        ),
        migrations.AlterField(
            model_name='monsterskilleffectdetail',
            name='target_hp',
            field=models.BooleanField(default=False, help_text="Amount of this effect is based on target monster's HP"),
        ),
        migrations.AlterField(
            model_name='runecraftinstance',
            name='quality',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')]),
        ),
        migrations.AlterField(
            model_name='runecraftinstance',
            name='rune',
            field=models.IntegerField(choices=[(1, 'Energy'), (2, 'Fatal'), (3, 'Blade'), (4, 'Rage'), (5, 'Swift'), (6, 'Focus'), (7, 'Guard'), (8, 'Endure'), (9, 'Violent'), (10, 'Will'), (11, 'Nemesis'), (12, 'Shield'), (13, 'Revenge'), (14, 'Despair'), (15, 'Vampire'), (16, 'Destroy'), (17, 'Fight'), (18, 'Determination'), (19, 'Enhance'), (20, 'Accuracy'), (21, 'Tolerance')]),
        ),
        migrations.AlterField(
            model_name='runecraftinstance',
            name='stat',
            field=models.IntegerField(choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')]),
        ),
        migrations.AlterField(
            model_name='runecraftinstance',
            name='type',
            field=models.IntegerField(choices=[(0, 'Grindstone'), (1, 'Enchant Gem')]),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='innate_stat',
            field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='main_stat',
            field=models.IntegerField(choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')]),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='original_quality',
            field=models.IntegerField(blank=True, choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='quality',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')], default=0),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_1',
            field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_1_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_2',
            field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_2_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_3',
            field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_3_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_4',
            field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_4_craft',
            field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem')], null=True),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_crafts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(0, 'Grindstone'), (1, 'Enchant Gem')], null=True), blank=True, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True), blank=True, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='type',
            field=models.IntegerField(choices=[(1, 'Energy'), (2, 'Fatal'), (3, 'Blade'), (4, 'Rage'), (5, 'Swift'), (6, 'Focus'), (7, 'Guard'), (8, 'Endure'), (9, 'Violent'), (10, 'Will'), (11, 'Nemesis'), (12, 'Shield'), (13, 'Revenge'), (14, 'Despair'), (15, 'Vampire'), (16, 'Destroy'), (17, 'Fight'), (18, 'Determination'), (19, 'Enhance'), (20, 'Accuracy'), (21, 'Tolerance')]),
        ),
        migrations.AlterField(
            model_name='storage',
            name='cloth',
            field=models.IntegerField(default=0, help_text='Thick Cloth'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_dark',
            field=models.IntegerField(default=0, help_text='Pitch-black Dark Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_fire',
            field=models.IntegerField(default=0, help_text='Flaming Fire Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_light',
            field=models.IntegerField(default=0, help_text='Shiny Light Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_magic',
            field=models.IntegerField(default=0, help_text='Condensed Magic Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_pure',
            field=models.IntegerField(default=0, help_text='Pure Magic Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_water',
            field=models.IntegerField(default=0, help_text='Frozen Water Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='crystal_wind',
            field=models.IntegerField(default=0, help_text='Whirling Wind Crystal'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='dark_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Dark Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='dust',
            field=models.IntegerField(default=0, help_text='Magic Dust'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='fire_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Fire Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='leather',
            field=models.IntegerField(default=0, help_text='Tough Leather'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='light_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Light Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='magic_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Magic Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='mithril',
            field=models.IntegerField(default=0, help_text='Shining Mythril'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='ore',
            field=models.IntegerField(default=0, help_text='Solid Iron Ore'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='rock',
            field=models.IntegerField(default=0, help_text='Solid Rock'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='rune_piece',
            field=models.IntegerField(default=0, help_text='Rune Piece'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='symbol_chaos',
            field=models.IntegerField(default=0, help_text='Symbol of Chaos'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='symbol_harmony',
            field=models.IntegerField(default=0, help_text='Symbol of Harmony'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='symbol_transcendance',
            field=models.IntegerField(default=0, help_text='Symbol of Transcendance'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='water_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Water Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='wind_essence',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], help_text='Wind Essence', size=3),
        ),
        migrations.AlterField(
            model_name='storage',
            name='wood',
            field=models.IntegerField(default=0, help_text='Hard Wood'),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='server',
            field=models.IntegerField(blank=True, choices=[(0, 'Global'), (1, 'Europe'), (2, 'Asia'), (3, 'Korea'), (4, 'Japan'), (5, 'China')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='America/Los_Angeles'),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, help_text='<a href="https://daringfireball.net/projects/markdown/syntax" target="_blank">Markdown syntax</a> enabled', null=True),
        ),
    ]
