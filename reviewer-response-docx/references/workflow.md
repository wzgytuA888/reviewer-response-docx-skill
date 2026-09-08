# Reviewer-response workflow

Use this workflow for each revision round. The local-data gate prevents analytical claims from being drafted before the underlying files and reproducible outputs are available.

```mermaid
flowchart TB
    accTitle: Scientific manuscript revision and reviewer-response workflow
    accDescr: The workflow diagnoses reviewer concerns, routes comments that need local data through author path collection and reproducible supplementary analysis, then verifies the revised manuscript and response package.

    subgraph intake["Intake and diagnosis"]
        start([Start revision round]) --> inspect[Inspect decision, reviews, manuscript, supplement, figures, tables, data, code, and prior format]
        inspect --> tracker[Build comment and evidence tracker]
        tracker --> diagnose[Diagnose the underlying scientific or presentation concern]
        diagnose --> data_needed{Does a defensible response require local data or reanalysis?}
    end

    subgraph evidence["Evidence route"]
        data_needed -- No --> literature[Verify literature and map the reader-facing revision]
        data_needed -- Yes --> paths_known{Are exact data and code paths available?}
        paths_known -- No --> ask_author[Ask the author for data, code, definitions, outputs, and environment paths]
        ask_author --> pending[Mark AUTHOR_INPUT_NEEDED_DATA_PATH and continue independent work]
        pending --> paths_known
        paths_known -- Yes --> inventory[Inspect read-only, inventory provenance, and preserve originals]
        inventory --> reproduce[Reproduce the reported baseline]
        reproduce --> analyze[Run and document supplementary analysis]
        analyze --> validate_data[Validate results across outputs, tables, figures, and text]
    end

    subgraph revision["Integrated revision"]
        literature --> revise[Revise the manuscript around its argument and verified evidence]
        validate_data --> revise
        revise --> respond[Draft the point-by-point response with exact revision excerpts and locations]
    end

    subgraph quality["Package verification"]
        respond --> verify[Check comment coverage, formatting, citations, locations, variants, and completion claims]
        verify --> unresolved{Does any blocking item remain?}
        unresolved -- Yes --> draft[Return a visible draft or author-input status]
        draft --> diagnose
        unresolved -- No --> ready([Return ready_to_submit])
    end

    classDef action fill:#e8f1fb,stroke:#2563eb,color:#172554
    classDef decision fill:#fff4cc,stroke:#b7791f,color:#4a2c00
    classDef status fill:#e8f7ee,stroke:#238636,color:#12351f

    class inspect,tracker,diagnose,literature,ask_author,inventory,reproduce,analyze,validate_data,revise,respond,verify action
    class data_needed,paths_known,unresolved decision
    class start,pending,draft,ready status
```

The loop from `AUTHOR_INPUT_NEEDED_DATA_PATH` resumes only after the author supplies usable paths. An explicit author decision to postpone the item changes its status to `DEFERRED_BY_AUTHOR`; it does not make the package submission-ready.
