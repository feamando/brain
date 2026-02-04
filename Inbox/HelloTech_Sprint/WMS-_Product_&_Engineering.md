---
type: hellotech_sprint_report
squad: WMS- Product & Engineering
tribe: Inventory Management
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907548
source: HelloTech Every Other Week Squad Sprint Report
---

## WMS- Product & Engineering
**Tribe:** Inventory Management
**Mega-Alliance:** Ops
**Squad Lead:** Eng: Ashraf Ali
PO:  Piotr Jastrzębski FCMS 
 Edwin Chung WMS2.0  
Owen Cascante-Rovira WMS-NA

### Squad KPI
WMS SCOS Compliance, P500 expansion/ AZ Pilot, Factor_, Inventory Accuracy/Cost

### KPI Movement
SCOS: Factor_EU Inbound operations launched on WMS-NA product in Verden, Germany 
P500: Several software deliveries around integration and WMS Workflow

### Delivered (This Sprint)
WMS2.0
1.UAT completed for Jan 21 product release
2. Demo held for partial pallet replen
WMS-NA
1.RF Translations for words in architect.(2h)
2.Prevent Partial Pallet move with different UOM EA/CS.(35h)
3. Remove additional screen during the Kit Receipt RF Process(4h)
4.Factor EU Weight sampling from LBS to KG(35h)
5.Performance tuning on WO import process(15h)
6.Changes to CPT workflow to display item description during dropoff(6h)
7.RF and web profile updates for LDL scan to slot(5h)
8.Slotting replens based on Proc subs tool Import(60h)
9.Item status validation for factor scanned item(2h)
10.International date format - Factor EU(9h)
11.Enhancements(filters) autostore Inventory Summary page(1h)
12. System Translation from English to German(27h)
13.PIO Inventory Dashboard and Return pages(26h)
14.Fix Item slot description filter - Autostore replens page(1h)
15.Kit Misc LP having both MLK and R sku code(8.5h)
16.Create tran log linking autostore import(21.5h)
17.Import and Process RPD data(61h)
18.Display correct UOM on Kit Replen Page(cs vs PL)-25.5h
FCMS
1.Continued design feedback on FCMS-WMS2.0 integration requirements to DAI
2. Improved UX flow of manual loc stock audit
3. Decoupled trolley trip generation from replen generation in background process to increase the  efficiency of multishuttle trolley trips
4. Functionality to adjust # of cases in Pallet Replen before deletion
5. Cleardown: show a list of the pallets with an SKU that can be scanned
6. Cleardown: UX adjustment of manual pallet creation flow
7. Cleardown: prevent mix of a stock with different BBD on the same pallet
8. Cleardown: allow to  search by SKU name or code within picking stations cleardown flow
9. Allow Picking Station Cleardown when there is picking activity ongoing on onther station belonging to the same line

### Planned (Next Sprint)
WMS2.0
1.Auto-populate BBD for undated PHF skus(IT)
2.Pre-Populateed list of allergens(IT)
3.BBD vs MLOR validation at palletisation(Bjuv)
4.Add Print LP button on Add LP page(Bjuv)
5.Make weight QC optional for all categories(Bjuv)
6.ICS-Create new transaction type for faild skus during QC(Bjuv)
7.Add questions on logo and control code for Organic products(Bjuv)
8.Sort Alphabetically on empty crates page.
9.Rename 'Yes' to 'Confirm' buttons in inbound.
WMS-NA
1.Return from Manufacturing partial LP's to include PO# and lot code.
2.PIO Message integration-wms integration service
3.Item sub forklift wo integration
4.Slotting & Replen process change for PIO.
5.Prevent dropping non-pio tasks into PIO staging locations.
6.Job to delete cycle log.
7.WO Picking - tune pick path sequence.
8.Putaway allergen violation- prevent items with allergens placed in adjacent locations.
9.Increase allergen attribute.
10.PIO Message Integration.
11.Cart Building for PIO kits and cart putaway.
12.Add item no to Case replens RF
13. Fix replen process for Autostore.
FCMS
1.Internal testing kickoff for thawing workflow enhancements

### Key Learnings
Streamling deployments for sprints, need for a checklist for migrations to sync objects ,test migrations.

**Demo:** Partial Pallet Replen