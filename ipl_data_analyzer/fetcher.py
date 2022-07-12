import csv
from ipl_data_analyzer.models import Matches, Deliveries


class CsvFetcher():

    def fetchMatchesDataFile(matches_file_path):
        matches_file = open(matches_file_path, encoding='unicode-escape')
        csv_reader_matches = csv.DictReader(matches_file)
        for match in csv_reader_matches:
            instance_of_matches_data_model = Matches(
                id=int(match['id']),
                season=match['season'],
                city=match['city'],
                date=match['date'],
                team1=match['team1'],
                team2=match['team2'],
                toss_winner=match['toss_winner'],
                toss_decision=match['toss_decision'],
                result=match['result'],
                dl_applied=match['dl_applied'],
                winner=match['winner'],
                win_by_runs=match['win_by_runs'],
                win_by_wickets=match['win_by_wickets'],
                player_of_match=match['player_of_match'],
                venue=match['venue'],
                umpire1=match['umpire1'],
                umpire2=match['umpire2'],
                umpire3=match['umpire3'],
            )
            instance_of_matches_data_model.save()
        print('MATCHES-DATA-STORED')

    def fetchDeliveriesDataFile(deliveries_file_path):
        deliveries_file = open(deliveries_file_path, encoding='unicode-escape')
        csv_reader_deliveries = csv.DictReader(deliveries_file)
        for match in csv_reader_deliveries:

            instance_of_deliveries_data_model = Deliveries(
                match_id=Matches.objects.get(id=int(match['match_id'])),
                inning=match['inning'],
                batting_team=match['batting_team'],
                bowling_team=match['bowling_team'],
                over=match['over'],
                ball=match['ball'],
                batsman=match['batsman'],
                non_striker=match['non_striker'],
                bowler=match['bowler'],
                is_super_over=match['is_super_over'],
                wide_runs=match['wide_runs'],
                bye_runs=match['bye_runs'],
                legbye_runs=match['legbye_runs'],
                noball_runs=match['noball_runs'],
                penalty_runs=match['penalty_runs'],
                batsman_runs=match['batsman_runs'],
                extra_runs=match['extra_runs'],
                total_runs=match['total_runs'],
                player_dismissed=match['player_dismissed'],
                dismissal_kind=match['dismissal_kind'],
                fielder=match['fielder'],
            )
            instance_of_deliveries_data_model.save()

            # match_id = int(match['match_id']),
            # id = Matches.objects.get(id=int(match['match_id'])),
            # match_id = int(match['match_id']),
            # match_id = Deliveries.objects.get(match_id=int(match['match_id'])),

        print('DELIVERIES-DATA-STORED')
