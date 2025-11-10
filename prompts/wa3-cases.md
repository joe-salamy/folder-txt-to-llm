# Prompt: Legal Case Analysis

## Context

You are an AI assistant helping a law student with a legal research and writing assignment. Your goal is to analyze a provided legal case according to a specific framework.

> **Critical Constraint:** You must adhere _strictly_ to the text of the case provided by the user. Do not reference, search for, or incorporate _any_ outside materials, definitions, or external context. Your entire analysis must be based _only_ on the provided text.

## Your Task

I will provide you with the text of a legal case. Once I provide the case, you will perform the following two requests based _only_ on that text.

---

### Request 1: Case Summary

Provide a brief summary of the case. **Your summary must begin with the case name as an h3 header.**

After the header, organize your summary into the following four sections. **All other text in your response (for both Request 1 and Request 2) should be normal paragraph text, not headers.** You should, however, continue to use formatting such as **bolding** (e.g., for section titles like **Facts:**), _italics_, and lists as appropriate for clarity.

- **Facts:** A concise overview of the relevant facts of the case.
- **Holding:** The court's final decision or answer to the question presented.
- **Reasoning:** The legal principles and logic the court used to reach its holding.
- **Significance:** The primary legal takeaway or rule established or affirmed by the case (as evidenced _in the text_).

---

### Request 2: Analysis of "Appropriation of a Partnership Opportunity"

Analyze the provided case _only_ through the lens of the "appropriation of a partnership opportunity" doctrine, as defined by **Cal. Corp. Code § 16404(b)(1)**.

This doctrine has two key elements (per _Kelegian v. Mgrdichian_, 33 Cal.App.4th 982, 988 (1995)):

1.  Whether the activity was “reasonably incident to the [partnership’s] present or prospective business.”
2.  Whether it was an activity “in which the [partnership] has the capacity to engage.”

For this analysis, you must complete the following steps:

1.  **Identify Discussion:** State clearly whether the case discusses **both** elements, **only one** (and which one), or **neither** element.
2.  **Extract Reasoning & Facts:** For _each_ element that the case _does_ discuss:
    - Identify and explain the court's **reasoning** related to that element.
    - Identify the specific **determinative facts** the court relied on to apply that element.
3.  **Synthesize Insight:** Conclude by stating what specific insight this case adds to the definition of the elements it discusses. You must follow the exact models below for your conclusion:
    - **For element 1:** "An activity is “reasonably incident to the [partnership’s] present or prospective business” when…"
    - **For element 2:** "A [partnership] has the capacity to engage in an activity when…"
