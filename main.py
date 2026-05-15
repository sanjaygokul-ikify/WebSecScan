import argparse

from src.scanner import Scanner


def main():
    parser = argparse.ArgumentParser(description='WebSecScan')
    parser.add_argument('--url', required=True, help='URL of web application to scan')
    parser.add_argument('--output-file', required=True, help='file to write scan results to')
    args = parser.parse_args()

    vulnerabilities = Scanner(args.url).scan()

    with open(args.output_file, 'w') as f:
        for vulnerability in vulnerabilities:
            f.write(vulnerability + '\n')


if __name__ == '__main__':
    main()
