import argparse


def get_data_processing_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--linkedin_email")
    parser.add_argument("--linkedin_password")
    parser.add_argument("--s3_path")


    return parser
