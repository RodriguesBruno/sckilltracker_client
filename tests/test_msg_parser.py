from src.msg_parser import (
    get_log_date,
    get_victim_player_name,
    get_killed_by, get_victim_zone,
    get_using,
    get_damage,
    get_game_mode,
    get_ship_name,
    get_pilot_name
)

from tests.conftest import log_entry


def test_get_log_date_returns_date():

    result = get_log_date(log_entry)

    expected_result = '2025-04-02 21:29:47 UTC'
    assert result == expected_result

def test_get_victim_player_name_returns_player_name():

    entry = "<2025-04-03T01:26:11.622Z> [Notice] <Actor Death> CActor::Kill: 'beast3PO' [200146293833] in zone 'AEGS_Gladius_2456589863667' killed by 'BluePanda' [202139681949] using 'KLWE_LaserRepeater_S2_2472796603691' [Class unknown] with damage type 'VehicleDestruction' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_victim_player_name(entry)

    expected_result = 'beast3PO'
    assert result == expected_result

def test_get_killed_by_return_player_name():
    result = get_killed_by(log_entry)

    expected_result = 'BlackHole'
    assert result == expected_result

# [VICTIM ZONE]
def test_get_victim_zone_in_station_return_station_name():
    result = get_victim_zone(log_entry)

    expected_result = 'OOC Stanton 1b Aberdeen'
    assert result == expected_result

def test_get_victim_zone_in_ship_return_ship_name():

    entry = "<2025-04-02T21:34:55.219Z> [Notice] <Actor Death> CActor::Kill: 'nocxua' [200146293087] in zone 'ANVL_Hornet_F7C_Mk2_2468344906962' killed by 'BluePanda' [202139681949] using 'MRCK_S03_AEGS_Sabre_Firebird_2470687086457' [Class unknown] with damage type 'VehicleDestruction' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_victim_zone(entry)

    expected_result = 'Hornet F7C Mk2'
    assert result == expected_result

def test_get_victim_zone_with_object_container_returns_zone_without_prefix():

    entry = "<2025-04-08T14:03:01.379Z> [Notice] <Actor Death> CActor::Kill: 'CBCORP' [2542505084000] in zone 'ObjectContainer-Newbab_Hab_Tower_Int_001' killed by 'CBCORP' [2542505084000] using 'CBCORP' [Class Player] with damage type 'Suicide' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_victim_zone(entry)

    expected_result = 'Newbab Hab Tower Int'
    assert result == expected_result

def test_get_victim_zone_with_object_container_with_underscore_returns_zone_without_prefix():

    entry = "<2025-04-08T14:03:01.379Z> [Notice] <Actor Death> CActor::Kill: 'CBCORP' [2542505084000] in zone 'ObjectContainer_habs' killed by 'CBCORP' [2542505084000] using 'CBCORP' [Class Player] with damage type 'Suicide' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_victim_zone(entry)

    expected_result = 'habs'
    assert result == expected_result

def test_get_victim_zone_in_lobby_returns_zone_without_prefix():

    entry = "<2025-04-08T14:04:29.799Z> [Notice] <Actor Death> CActor::Kill: 'CBCORP' [2542505084000] in zone 'ObjectContainer-Ground_Lobby' killed by 'CBCORP' [2542505084000] using 'CBCORP' [Class Player] with damage type 'Suicide' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_victim_zone(entry)

    expected_result = 'Ground Lobby'
    assert result == expected_result

# [USING]
def test_get_using_returns_weapon_name():
    result = get_using(log_entry)

    expected_result = 'BFG'
    assert result == expected_result

def test_get_using_with_big_name_returns_weapon_name():

    entry ="<2025-04-02T21:34:55.219Z> [Notice] <Actor Death> CActor::Kill: 'nocxua' [200146293087] in zone 'ANVL_Hornet_F7C_Mk2_2468344906962' killed by 'BluePanda' [202139681949] using 'MRCK_S03_AEGS_Sabre_Firebird_2470687086457' [Class unknown] with damage type 'VehicleDestruction' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_using(entry)

    expected_result = 'MRCK S03 AEGS Sabre Firebird'
    assert result == expected_result

def test_get_using_from_crash_returns_dash():

    entry = "<2025-04-08T13:53:00.119Z> [Notice] <Actor Death> CActor::Kill: 'CBCORP' [2542505084000] in zone 'RSI_Aurora_MR_2577693134594' killed by 'CBCORP' [2542505084000] using 'unknown' [Class unknown] with damage type 'Crash' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_using(entry)

    expected_result = '-'
    assert result == expected_result

# [DAMAGE]

def test_get_damage_returns_damage_type():
    result = get_damage(log_entry)

    expected_result = 'Fire'
    assert result == expected_result


def test_get_damage_with_vehicle_destruction_returns_vehicle_destruction():
    entry = "<2025-04-02T21:34:55.219Z> [Notice] <Actor Death> CActor::Kill: 'nocxua' [200146293087] in zone 'ANVL_Hornet_F7C_Mk2_2468344906962' killed by 'BluePanda' [202139681949] using 'MRCK_S03_AEGS_Sabre_Firebird_2470687086457' [Class unknown] with damage type 'VehicleDestruction' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_damage(entry)

    expected_result = 'Vehicle Destruction'
    assert result == expected_result

def test_get_damage_with_bullet_returns_bullet():
    entry = "<2025-04-08T22:36:40.104Z> [Notice] <Actor Death> CActor::Kill: 'Fr33' [201964490746] in zone 'util_a_orbital_001_occu_a_final_int' killed by 'BluePanda' [202139681949] using 'behr_lmg_ballistic_01_2529333258789' [Class behr_lmg_ballistic_01] with damage type 'Bullet' from direction x: -0.883246, y: 0.152149, z: -0.443540 [Team_ActorTech][Actor]"
    result = get_damage(entry)

    expected_result = 'Bullet'
    assert result == expected_result

def test_get_damage_with_crash_returns_crash():
    entry = "<2025-04-08T23:16:39.092Z> [Notice] <Actor Death> CActor::Kill: 'BluePanda' [202139681949] in zone 'ANVL_Hornet_F7A_Mk2_2583529927313' killed by 'BluePanda' [202139681949] using 'unknown' [Class unknown] with damage type 'Crash' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_damage(entry)

    expected_result = 'Crash'
    assert result == expected_result

# [GAME MODE]

def test_get_game_mode_persistence_universe_returns_type_persistence_universe():

    entry = '<2025-04-08T10:43:32.228Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="WaitForConnectionEstablished" state=eCVS_Initial(0) status="Finished" runningTime=0.000001 numRuns=1 map="megamap" gamerules="SC_Frontend" sessionId="f052f409d378f05d5266d6cd379d5db0" [Team_Network][Network][Replication][Loading][Persistence]'
    result = get_game_mode(entry)

    expected_result = 'PU'
    assert result == expected_result

def test_get_game_mode_classic_race_returns_type_classic_race():

    entry = '<2025-04-07T16:00:41.941Z> [Notice] <[EALobby] EALobbyChangeMode> [EALobby][CEALobby::RequestChangeGameMode] BluePanda Requesting Mode Change from INVALID[-1] to EA_ClassicRace[5] | PlayerChoice[0] [Team_ArenaCommanderFeature][Code][EA]'
    result = get_game_mode(entry)

    expected_result = 'Classic Race'
    assert result == expected_result

def test_get_game_mode_fps_gun_game_returns_type_gun_rush():

    entry = '<2025-04-08T11:33:08.190Z> [Notice] <Context Establisher Done> establisher="CReplicationModel" runningTime=7.574790 map="megamap" gamerules="EA_FPSGunGame" sessionId="69f6f376-c622-8e44-90ba-4836a49aa3de" [Team_Network][Network][Replication][Loading][Persistence]'
    result = get_game_mode(entry)

    expected_result = 'Gun Rush'
    assert result == expected_result

def test_get_game_mode_squadron_battle_returns_type_squadron_battle():

    entry = '<2025-04-07T15:59:41.087Z> [Notice] <[EALobby] EALobbyChangeMode> [EALobby][CEALobby::RequestChangeGameMode] BluePanda Requesting Mode Change from GameMode.EA_ClassicRace[5] to EA_SquadronBattle[3] | PlayerChoice[1] [Team_ArenaCommanderFeature][Code][EA]'
    result = get_game_mode(entry)

    expected_result = 'Squadron Battle'
    assert result == expected_result

def test_get_game_mode_team_elimination_returns_type_team_elimination():

    entry = '<2025-04-08T10:41:10.422Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="InitView.ClientPlayer" state=eCVS_InGame(16) status="Finished" runningTime=0.000077 numRuns=1 map="megamap" gamerules="EA_TeamElimination" sessionId="f052f409d378f05d5266d6cd379d5db0" [Team_Network][Network][Replication][Loading][Persistence]'
    result = get_game_mode(entry)

    expected_result = 'Team Elimination'
    assert result == expected_result

def test_get_game_mode_free_flight_returns_type_free_flight():

    entry = '<2025-04-08T11:20:04.940Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="InitView.ClientPlayer" state=eCVS_InGame(16) status="Finished" runningTime=0.000063 numRuns=1 map="megamap" gamerules="EA_FreeFlight" sessionId="f052f409d378f05d5266d6cd379d5db0" [Team_Network][Network][Replication][Loading][Persistence]'
    result = get_game_mode(entry)

    expected_result = 'Free Flight'
    assert result == expected_result

def test_get_game_mode_experimental_type_3_returns_type_tank_royal():

    entry = '<2025-04-08T13:27:55.760Z> [Notice] <[EALobby] EALobbyChangeMode> [EALobby][CEALobby::RequestChangeGameMode] CBCORP Requesting Mode Change from GameMode.EA_ClassicRace[5] to EA_ExperimentalMode_3[17] | PlayerChoice[1] [Team_ArenaCommanderFeature][Code][EA]'
    result = get_game_mode(entry)

    expected_result = 'Tank Royale'
    assert result == expected_result

def test_get_game_mode_with_new_mode_returns_type_new_mode():

    entry = '<2025-04-07T15:59:41.087Z> [Notice] <[EALobby] EALobbyChangeMode> [EALobby][CEALobby::RequestChangeGameMode] BluePanda Requesting Mode Change from GameMode.EA_ClassicRace[5] to EA_NewExperimentalMode[3] | PlayerChoice[1] [Team_ArenaCommanderFeature][Code][EA]'
    result = get_game_mode(entry)

    expected_result = 'New Experimental Mode'
    assert result == expected_result

def test_get_game_mode_from_sc_to_main_menu_returns_type_pu():

    entry = '<2025-04-08T13:18:22.423Z> [Notice] <[EALobby] EALobbyChangeMode> [EALobby][CEALobby::RequestChangeGameMode] CBCORP Requesting Mode Change from INVALID[-1] to EA_ExperimentalMode_3[17] | PlayerChoice[0] [Team_ArenaCommanderFeature][Code][EA]'
    result = get_game_mode(entry)

    expected_result = 'PU'
    assert result == expected_result

# [SHIP NAME]

def test_ship_name_in_squadron_battle_returns_ship_name():

    entry ="<2025-04-08T22:01:11.249Z> [VEHICLE SPAWN] CPlayerShipRespawnManager::OnVehicleSpawned 200000001483 (RSI_Aurora_MR_200000001483) by player 2542505084000"
    result = get_ship_name(entry)

    expected_result = 'Aurora MR'
    assert result == expected_result


def test_ship_name_in_pu_returns_ship_name():

    entry ="<2025-04-08T15:24:39.695Z> [Notice] <Jump Drive Requesting State Change> Requested change from Idle to Idle, reason: Jump Drive is no longer in use [linked to no jump point] | CL26524 | NOT AUTH | Stanton | JDRV_TARS_S01_Explorer_SCItem_2516120332809 [2516120332809] (adam: ANVL_Hornet_F7A_Mk2_2516120332762 in zone Hangar_SmallTop_RestStop_2567616145532) | CSCItemJumpDrive::SetState [Team_VehicleFeatures][JumpSystem]"
    result = get_ship_name(entry)

    expected_result = 'Hornet F7A Mk2'
    assert result == expected_result

def test_get_ship_name_with_hornet_returns_hornet_f7a():

    entry = "<2025-04-02T21:34:55.219Z> [Notice] <Actor Death> CActor::Kill: 'nocxua' [200146293087] in zone 'ANVL_Hornet_F7C_Mk2_2468344906962' killed by 'BluePanda' [202139681949] using 'MRCK_S03_AEGS_Sabre_Firebird_2470687086457' [Class unknown] with damage type 'VehicleDestruction' from direction x: 0.000000, y: 0.000000, z: 0.000000 [Team_ActorTech][Actor]"
    result = get_ship_name(entry)

    expected_result = 'Hornet F7C Mk2'
    assert result == expected_result
#
# def test_get_ship_name_with_lightning_returns_lighting():
#
#     entry = '<2025-04-03T01:39:19.687Z> [Notice] <Jump Drive State Changed> Now Idle | CL11556 | NOT AUTH | Stanton | JDRV_TARS_S01_Explorer_SCItem_2472796603665 [2472796603665] (adam: ANVL_Lightning_F8C_2472796603606 in zone OOC_Stanton_2b_Daymar) | CSCItemJumpDrive::OnStateChanged [Team_VehicleFeatures][JumpSystem]'
#     result = get_ship_name(entry)
#
#     expected_result = 'Lightning F8C'
#     assert result == expected_result
#
# def test_get_ship_name_with_gladius_returns_gladius():
#
#     entry = '<2025-04-07T16:00:05.234Z> [Notice] <Jump Drive State Changed> Now Idle | CL19240 | NOT AUTH | DefaultSolarSystem | JDRV_TARS_S01_Explorer_SCItem_2562525120629 [2562525120629] (adam: JDRV_TARS_S01_Explorer_SCItem_2562525120629 in zone AEGS_Gladius_2562525120585) | CSCItemJumpDrive::OnStateChanged [Team_VehicleFeatures][JumpSystem]'
#     result = get_ship_name(entry)
#
#     expected_result = 'Gladius'
#     assert result == expected_result

# def test_get_ship_name_with_aurora_mr_returns_aurora_mr():
#
#     entry = '<2025-04-08T09:15:13.395Z> [VEHICLE SPAWN] CPlayerShipRespawnManager::OnVehicleSpawned 200000001483 (RSI_Aurora_MR_200000001483) by player 2542505084000'
#     result = get_ship_name(entry)
#
#     expected_result = 'Aurora MR'
#     assert result == expected_result
#
# def test_get_ship_name_with_argo_mr_returns_argo():
#
#     entry = '<2025-04-08T10:13:37.944Z> [VEHICLE SPAWN] CPlayerShipRespawnManager::OnVehicleSpawned 200000026367 (ARGO_MPUV_1T_200000026367) by player 2542505084000 '
#     result = get_ship_name(entry)
#
#     expected_result = 'MPUV 1T'
#     assert result == expected_result

# [PILOT NAME]

def test_get_pilot_name_returns_pilot_name():
    entry = '<2025-04-07T15:59:37.784Z> [Notice] <OnClientConnected> Player[RedPanda] has connected. [Team_ActorFeatures][Inventory]'
    result = get_pilot_name(entry)

    expected_result = 'RedPanda'
    assert result == expected_result

def test_get_pilot_name_with_another_name_returns_pilot_name():
    entry = '<2025-04-08T08:42:39.869Z> [Notice] <OnClientConnected> Player[CBCORP] has connected. [Team_ActorFeatures][Inventory]'
    result = get_pilot_name(entry)

    expected_result = 'CBCORP'
    assert result == expected_result

def test_get_pilot_name_with_long_name_returns_pilot_name():
    entry = '<2025-04-07T15:59:37.784Z> [Notice] <OnClientConnected> Player[ThisNameIsWeird] has connected. [Team_ActorFeatures][Inventory]'
    result = get_pilot_name(entry)

    expected_result = 'ThisNameIsWeird'
    assert result == expected_result