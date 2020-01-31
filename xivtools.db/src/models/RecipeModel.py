from marshmallow import fields, Schema
from . import db


class RecipeModel(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    crafttype = db.Column(db.Text)
    recipeleveltable = db.Column(db.SMALLINT)
    itemresult = db.Column(db.Text)
    amountresult = db.Column(db.SMALLINT)
    itemingredient0 = db.Column(db.Text)
    amountingredient0 = db.Column(db.SMALLINT)
    itemingredient1 = db.Column(db.Text)
    amountingredient1 = db.Column(db.SMALLINT)
    itemingredient2 = db.Column(db.Text)
    amountingredient2 = db.Column(db.SMALLINT)
    itemingredient3 = db.Column(db.Text)
    amountingredient3 = db.Column(db.SMALLINT)
    itemingredient4 = db.Column(db.Text)
    amountingredient4 = db.Column(db.SMALLINT)
    itemingredient5 = db.Column(db.Text)
    amountingredient5 = db.Column(db.SMALLINT)
    itemingredient6 = db.Column(db.Text)
    amountingredient6 = db.Column(db.SMALLINT)
    itemingredient7 = db.Column(db.Text)
    amountingredient7 = db.Column(db.SMALLINT)
    itemingredient8 = db.Column(db.Text)
    amountingredient8 = db.Column(db.SMALLINT)
    itemingredient9 = db.Column(db.Text)
    amountingredient9 = db.Column(db.SMALLINT)
    unk25 = db.Column(db.SMALLINT)
    issecondary = db.Column(db.Boolean)
    materialqualityfactor = db.Column(db.SMALLINT)
    difficultyfactor = db.Column(db.SMALLINT)
    qualityfactor = db.Column(db.SMALLINT)
    durabilityfactor = db.Column(db.SMALLINT)
    unk31 = db.Column(db.SMALLINT)
    requiredcraftsmanship = db.Column(db.SMALLINT)
    requiredcontrol = db.Column(db.SMALLINT)
    quicksynthcraftsmanship = db.Column(db.SMALLINT)
    quicksynthcontrol = db.Column(db.SMALLINT)
    secretrecipebook = db.Column(db.Text)
    canquicksynth = db.Column(db.Boolean)
    canhq = db.Column(db.Boolean)
    exprewarded = db.Column(db.Boolean)
    statusrequired = db.Column(db.Text)
    itemrequired = db.Column(db.Text)
    isspecializationrequired = db.Column(db.Boolean)
    unk43 = db.Column(db.Boolean)
    patchnumber = db.Column(db.SMALLINT)


    def __init__(self,data):
        self.id = data.get(id)
        self.number = data.get(number)
        self.crafttype = data.get(crafttype)
        self.recipeleveltable = data.get(recipeleveltable)
        self.itemresult = data.get(itemresult)
        self.amountresult = data.get(amountresult)
        self.itemingredient0 = data.get(itemingredient0)
        self.amountingredient0 = data.get(amountingredient0)
        self.itemingredient1 = data.get(itemingredient1)
        self.amountingredient1 = data.get(amountingredient1)
        self.itemingredient2 = data.get(itemingredient2)
        self.amountingredient2 = data.get(amountingredient2)
        self.itemingredient3 = data.get(itemingredient3)
        self.amountingredient3 = data.get(amountingredient3)
        self.itemingredient4 = data.get(itemingredient4)
        self.amountingredient4 = data.get(amountingredient4)
        self.itemingredient5 = data.get(itemingredient5)
        self.amountingredient5 = data.get(amountingredient5)
        self.itemingredient6 = data.get(itemingredient6)
        self.amountingredient6 = data.get(amountingredient6)
        self.itemingredient7 = data.get(itemingredient7)
        self.amountingredient7 = data.get(amountingredient7)
        self.itemingredient8 = data.get(itemingredient8)
        self.amountingredient8 = data.get(amountingredient8)
        self.itemingredient9 = data.get(itemingredient9)
        self.amountingredient9 = data.get(amountingredient9)
        self.unk25 = data.get(unk25)
        self.issecondary = data.get(issecondary)
        self.materialqualityfactor = data.get(materialqualityfactor)
        self.difficultyfactor = data.get(difficultyfactor)
        self.qualityfactor = data.get(qualityfactor)
        self.durabilityfactor = data.get(durabilityfactor)
        self.unk31 = data.get(unk31)
        self.requiredcraftsmanship = data.get(requiredcraftsmanship)
        self.requiredcontrol = data.get(requiredcontrol)
        self.quicksynthcraftsmanship = data.get(quicksynthcraftsmanship)
        self.quicksynthcontrol = data.get(quicksynthcontrol)
        self.secretrecipebook = data.get(secretrecipebook)
        self.canquicksynth = data.get(canquicksynth)
        self.canhq = data.get(canhq)
        self.exprewarded = data.get(exprewarded)
        self.statusrequired = data.get(statusrequired)
        self.itemrequired = data.get(itemrequired)
        self.isspecializationrequired = data.get(isspecializationrequired)
        self.unk43 = data.get(unk43)
        self.patchnumber = data.get(patchnumber)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_limit(n):
        return RecipeModel.query.limit(n)

    def get_one(id):
        return RecipeModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RecipeSchema(Schema):
    id = fields.Int(dump_only=True)
    number = fields.Int(required=True)
    crafttype = fields.Str(required=True)
    recipeleveltable = fields.Int(required=True)
    itemresult = fields.Str(required=True)
    amountresult = fields.Int(required=True)
    itemingredient0 = fields.Str(required=True)
    amountingredient0 = fields.Int(required=True)
    itemingredient1 = fields.Str(required=True)
    amountingredient1 = fields.Int(required=True)
    itemingredient2 = fields.Str(required=True)
    amountingredient2 = fields.Int(required=True)
    itemingredient3 = fields.Str(required=True)
    amountingredient3 = fields.Int(required=True)
    itemingredient4 = fields.Str(required=True)
    amountingredient4 = fields.Int(required=True)
    itemingredient5 = fields.Str(required=True)
    amountingredient5 = fields.Int(required=True)
    itemingredient6 = fields.Str(required=True)
    amountingredient6 = fields.Int(required=True)
    itemingredient7 = fields.Str(required=True)
    amountingredient7 = fields.Int(required=True)
    itemingredient8 = fields.Str(required=True)
    amountingredient8 = fields.Int(required=True)
    itemingredient9 = fields.Str(required=True)
    amountingredient9 = fields.Int(required=True)
    unk25 = fields.Int(required=True)
    issecondary = fields.Boolean(required=True)
    materialqualityfactor = fields.Int(required=True)
    difficultyfactor = fields.Int(required=True)
    qualityfactor = fields.Int(required=True)
    durabilityfactor = fields.Int(required=True)
    unk31 = fields.Int(required=True)
    requiredcraftsmanship = fields.Int(required=True)
    requiredcontrol = fields.Int(required=True)
    quicksynthcraftsmanship = fields.Int(required=True)
    quicksynthcontrol = fields.Int(required=True)
    secretrecipebook = fields.Str(required=True)
    canquicksynth = fields.Boolean(required=True)
    canhq = fields.Boolean(required=True)
    exprewarded = fields.Boolean(required=True)
    statusrequired = fields.Str(required=True)
    itemrequired = fields.Str(required=True)
    isspecializationrequired = fields.Boolean(required=True)
    unk43 = fields.Boolean(required=True)
    patchnumber = fields.Int(required=True)
