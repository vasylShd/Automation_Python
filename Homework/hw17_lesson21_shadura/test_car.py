import pytest
from .hw12_lesson16_shadura import ElectroCar


class TestElectroCar:
    electrocar_1 = ElectroCar('Chevrolet', 'Bolt EV', 'Red', 'Hatchback', 'Electric', 200, 70, 400)
    # brend, model, color, car_class, fuel_type, total_power, battery_capacity, mileage_per_charge_100_prcnt


    @pytest.mark.monkey_fixture
    def test_charge_time(self, electrocar, monkeypatch):
        monkeypatch.setattr(electrocar, 'battery_capacity', 70)
        electrocar.charge_time(35, 8)
        assert electrocar.charge_time_to_full == 5.6


    @pytest.mark.way_by_battery_proc
    @pytest.mark.parametrize('battery_remaining_prcnt, expected_result_km', [(40, 160),
                                                                             (80, 320),
                                                                             (100, 400)])
    def test_driving_faraway(self, battery_remaining_prcnt, expected_result_km):
        prcnt_battery_distance = TestElectroCar.electrocar_1.driving_faraway(battery_remaining_prcnt)
        assert prcnt_battery_distance == expected_result_km


    @pytest.mark.negative_test
    @pytest.mark.way_by_battery_proc
    def test_negative_driving_faraway(self):
        battery_remaining_prcnt = 50
        with pytest.raises(AssertionError):
            assert TestElectroCar.electrocar_1.driving_faraway(battery_remaining_prcnt) == 150


    @pytest.mark.negative_test
    @pytest.mark.xfail(reason='Failed, I know, the function has a bug (charge_time is not "6")', condition=True)
    def test_fail_charge_time(self):
        TestElectroCar.electrocar_1.charge_time(30, 10)
        assert  TestElectroCar.electrocar_1.charge_time_to_full == 6


    @pytest.mark.skip('functionality not implemened yet')
    @pytest.mark.monkey_fixture
    def test_charge_time_2(self, electrocar, monkeypatch):
        pass