from ui.ui_form import run_ui
from crawler.crawler import crawl_issues
from parser.parser import parse_issues
from generator.report_generator import generate_report
from exporter.file_exporter import export

def main():
    date = run_ui()
    htmls = crawl_issues(date)
    parsed = parse_issues(htmls)
    report = generate_report(parsed)
    export(report)

if __name__ == "__main__":
    main()