from src.event_manager import find_event_line


def test_find_event_line_with_game_mode_returns_something():

    keywords = ['> Loading screen for ', '> Mode[EA']

    lines = [
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="CReplicationModel" message="CET completed" taskname="WaitForTutorialMission" state=eCVS_InGame(16) status="Finished" runningTime=0.000005 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="ee6a06ca-ee67-f148-82ca-a4d8323dd4dd" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="CReplicationModel" message="CET completed" taskname="WaitForGameRulesSpawningModule" state=eCVS_InGame(16) status="Finished" runningTime=0.000014 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="ee6a06ca-ee67-f148-82ca-a4d8323dd4dd" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> Loading screen for pu : SC_Frontend closed after 30.00 seconds',
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="CReplicationModel" message="CET completed" taskname="StopLoadingScreen" state=eCVS_InGame(16) status="Finished" runningTime=0.000046 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="ee6a06ca-ee67-f148-82ca-a4d8323dd4dd" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <Context Establisher Done> establisher="CReplicationModel" runningTime=30.007910 map="megamap" gamerules="SC_Default" sessionId="ee6a06ca-ee67-f148-82ca-a4d8323dd4dd" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <Context Establisher Unblocked> establisher="Network" taskname="WaitRemoteState" state=eCVS_InGame(16) map="megamap" gamerules="SC_Default" sessionId="f2253b5c9f29d06f60c5a240313466d2" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="WaitRemoteState" state=eCVS_InGame(16) status="Finished" runningTime=0.000002 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="f2253b5c9f29d06f60c5a240313466d2" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="InitActionMap.ClientPlayer" state=eCVS_InGame(16) status="Finished" runningTime=0.000014 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="f2253b5c9f29d06f60c5a240313466d2" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <ContextEstablisherTaskFinished> establisher="Network" message="CET completed" taskname="InitView.ClientPlayer" state=eCVS_InGame(16) status="Finished" runningTime=0.000096 numRuns=1 map="megamap" gamerules="SC_Default" sessionId="f2253b5c9f29d06f60c5a240313466d2" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.908Z> [Notice] <Context Establisher Done> establisher="Network" runningTime=30.007990 map="megamap" gamerules="SC_Default" sessionId="f2253b5c9f29d06f60c5a240313466d2" [Team_Network][Network][Replication][Loading][Persistence]',
        '<2025-04-18T11:27:07.924Z> [Notice] <QueryInventory> Elapsed[0.516252] for IInventoryAPI::AsyncQueryInventory. [Team_ActorFeatures][Inventory]'
    ]

    result = find_event_line(lines=lines, keywords=keywords)

    expect_result = '<2025-04-18T11:27:07.908Z> Loading screen for pu : SC_Frontend closed after 30.00 seconds'

    assert result == expect_result