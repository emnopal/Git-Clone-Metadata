from utils.metadata import GitClone
import argparse


class Parse:

    @staticmethod
    def parse():

        default = "no"

        parser = argparse.ArgumentParser(description='Git Clone Info')

        parser.add_argument('--url',
                            type=str,
                            help='The URL',
                            required=True)

        parser.add_argument('--show',
                            type=str,
                            help='Show All',
                            default=default)

        parser.add_argument('--save',
                            type=str,
                            help='Save to JSON',
                            default=default)

        parser.add_argument('--clone',
                            type=str,
                            help='Cloning the Repository',
                            default=default)

        args = parser.parse_args()

        return args


if __name__ == "__main__":

    args = Parse.parse()
    git = GitClone(args.url)
    git.shows(args.show, args.save, args.clone)
