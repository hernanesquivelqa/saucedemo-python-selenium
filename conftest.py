import pytest


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    metadata = {"Project": "My Automation Tests", "Tester": "Pablo Esquivel", "Environment": "QA"}

    # Agregar cada metadato al reporte HTML
    for key, value in metadata.items():
        prefix.append(f"<p><strong>{key}:</strong> {value}</p>")
