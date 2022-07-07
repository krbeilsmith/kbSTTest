/*
A KBase module: kbeilsmithTestST
This sample module contains one small method that filters contigs.
*/

module kbeilsmithTestST {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_kbeilsmithTestST(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
