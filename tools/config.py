'''
NOTES:
ITEM: in exports change Lot to IsEquippable
'''

get = {
    "Action":["id","Name","Icon","ActionCategory","ClassJob","BehaviourType",
    "ClassJobLevel","IsRoleAction","Range","CanTargetSelf","CanTargetParty",
    "CanTargetFriendly","CanTargetHostile","TargetArea","CanTargetDead","CastType",
    "EffectRange","XAxisModifier","PrimaryCostType","PrimaryCostValue",
    "SecondaryCostType","SecondaryCostValue","ActionCombo","PreservesCombo",
    "Cast100ms","Recast100ms","CooldownGroup","MaxCharges","AttackType","Aspect",
    "ActionProcStatus","StatusGainSelf","UnlockLink","ClassJobCategory",
    "AffectsPosition","Omen","IsPvP","IsPlayerAction"],
    "ActionTransient":["id","Description"],
    "Item":["id","Singular","Adjective","Plural","PossessivePronoun",
    "StartsWithVowel","Pronoun","Article","Description","Name","Icon",
    "LevelItem","Rarity","FilterGroup","AdditionalData","ItemUICategory",
    "ItemSearchCategory","EquipSlotCategory","StackSize","IsUnique",
    "IsUntradable","IsIndisposable","IsEquippable","PriceMid","PriceLow",
    "CanBeHq","IsDyeable","IsCrestWorthy","ItemAction","Cooldowns",
    "ClassJobRepair","ItemRepair","ItemGlamour","Salvage","IsCollectable",
    "AlwaysCollectable","AetherialReduce","LevelEquip",
    "EquipRestriction","ClassJobCategory","GrandCompany","ItemSeries",
    "BaseParamModifier","ModelMain","ModelSub","ClassJobUse",
    "DamagePhys","DamageMag","Delayms","BlockRate","Block",
    "DefensePhys","DefenseMag","BaseParam0","BaseParamValue0","BaseParam1",
    "BaseParamValue1","BaseParam2","BaseParamValue2","BaseParam3",
    "BaseParamValue3","BaseParam4","BaseParamValue4","BaseParam5",
    "BaseParamValue5","ItemSpecialBonus","ItemSpecialBonusParam",
    "BaseParamSpecial0","BaseParamValueSpecial0","BaseParamSpecial1",
    "BaseParamValueSpecial1","BaseParamSpecial2","BaseParamValueSpecial2",
    "BaseParamSpecial3","BaseParamValueSpecial3","BaseParamSpecial4",
    "BaseParamValueSpecial4","BaseParamSpecial5","BaseParamValueSpecial5",
    "MaterializeType","MateriaSlotCount","IsAdvancedMeldingPermitted","IsPvP",
    "IsGlamourous"],
    "Recipe":["id","Number","CraftType","RecipeLevelTable","ItemResult","AmountResult",
    "ItemIngredient0","AmountIngredient0","ItemIngredient1","AmountIngredient1",
    "ItemIngredient2","AmountIngredient2","ItemIngredient3","AmountIngredient3",
    "ItemIngredient4","AmountIngredient4","ItemIngredient5","AmountIngredient5",
    "ItemIngredient6","AmountIngredient6","ItemIngredient7","AmountIngredient7",
    "ItemIngredient8","AmountIngredient8","ItemIngredient9","AmountIngredient9",
    "unK25","IsSecondary","MaterialQualityFactor","DifficultyFactor","QualityFactor",
    "DurabilityFactor","unK31","RequiredCraftsmanship","RequiredControl",
    "QuickSynthCraftsmanship","QuickSynthControl","SecretRecipeBook",
    "CanQuickSynth","CanHq","ExpRewarded","StatusRequired","ItemRequired",
    "IsSpecializationRequired","unK43","PatchNumber"],
    "RecipeLookup":["id","unK0","unK1","unK2","unK3","unK4","unK5","unK6","unK7"],
    "Status":[]
}

edit = {"Item":["EquipSlotCategory", "ItemAction", "ItemAction"],
        "Recipe":["RecipeLevelTable"]
}

lists = {"Item":["ModelMain", "ModelSub"]}
