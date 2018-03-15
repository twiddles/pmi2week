package org.teradata.dblp;

public class Publication {
    private String key;
    private String title;
    private String crossref;
    private String date;

    public Publication(String key, String title, String crossref, String date) {
        this.key = key;
        this.title = title;
        this.crossref = crossref;
        this.date = date;
    }

    public String getKey() {
        return key;
    }

    public String getTitle() {
        return title;
    }

    public String getCrossref() {
        return crossref;
    }

    public String getDate() {
        return date;
    }
}
